from toolz.dicttoolz import valfilter

from models import utilities
from models.Sheet import Sheet


class CLRProcessor:
    def __init__(self):
        self._loadedSheets = []
        self._parsedSheets = []
        self._codes = {}
        self._codesFilter = None
        self._rateFilter = None
        self._maxCountOfSheetsForCode = 1

    def addSheet(self, sheet):
        self._loadedSheets.append(sheet)

    def sheetFileAlreadyParsed(self, filepath):
        for sheet in self._parsedSheets:
            if sheet.fullFilePath == filepath:
                return True
        return False

    def setCodeFilter(self, destination, code):
        self._codesFilter = (destination, code)

    def clearCodeFilter(self):
        self._codesFilter = None

    def setRateFilter(self, rate):
        self._rateFilter = rate

    def clearRateFilter(self):
        self._rateFilter = None

    def buildCLR(self):
        self._loadSheetsData()
        print("CLR Errors: ", self.getErrors())

        if self._codesFilter:
            self._codes = {key: self._codes[key] for key in self._filterCodes()}
        if self._rateFilter:
            for code in self._codes:
                self._codes[code] = list(filter(lambda x: x[2] <= self._rateFilter, self._codes[code]))
            self._codes = valfilter(lambda x: len(x) > 0, self._codes)

        self._maxCountOfSheetsForCode = 1
        for code in self._codes:
            if len(self._codes[code]) > 1:
                self._codes[code] = sorted(self._codes[code], key=lambda x: x[2])
                if len(self._codes[code]) > self._maxCountOfSheetsForCode:
                    self._maxCountOfSheetsForCode = len(self._codes[code])

    def _filterCodes(self):
        dest, code = self._codesFilter
        dest = dest.strip().lower()
        code = code.strip()
        if code != "":
            if code.endswith('!'):
                filter =int(code[:-1])
                for key in self._codes.keys():
                    if key == filter:
                        yield key
            else:
                for key in self._codes.keys():
                    if str(key).startswith(code):
                        yield key
        elif dest != "":
            if dest.endswith('!'):
                for key in self._codes.keys():
                    if dest[:-1] == self._codes[key][0][1].lower():
                        yield key
            else:
                for key in self._codes.keys():
                    if self._codes[key][0][1].lower().startswith(dest):
                        yield key
        else:
            raise ValueError("The empty code filter was specified")

    def _loadSheetsData(self):
        self._clearErrors()
        self._codes = {}
        for sh in self._loadedSheets:
            if not sh.loaded:
                print(f"The sh {sh.fileName} was not loaded. Skipping")
                continue
            self._skipLinesCounter = 0
            if sh.dataFormat[3] > 0:
                self._extractСodesFromTableUsingDate(sh)
            else:
                self._extractСodesFromTable(sh)
            self._parsedSheets.append(sh)

    def _extractСodesFromTableUsingDate(self, sh):
        destColumn, codeColumn, rateColumn, dateColumn, startLine, endLine = sh.dataFormat
        for line in range(startLine, endLine + 1):
            destination = sh.worksheet.cell(row=line, column=destColumn).value
            code = sh.worksheet.cell(row=line, column=codeColumn).value
            rate = sh.worksheet.cell(row=line, column=rateColumn).value

            if not self._checkEmptyLines(code, rate):
                break

            lineError = False
            if not self._codeIsValid(code):
                self._addError(sh, line, codeColumn)
                lineError = True
            if not self._rateIsValid(rate):
                self._addError(sh, line, rateColumn)
                lineError = True
            if not self._destinationIsValid(destination):
                self._addError(sh, line, destColumn)

            date = sh.worksheet.cell(row=line, column=dateColumn).value
            if not lineError:
                data = (str(sh), destination, rate, date, line)
                key = int(code)

                if key in self._codes:
                    for i, li in enumerate(self._codes[key]):
                        if li[0] == str(sh):
                            if date > li[3]:
                                self._codes[key][i] = data
                            break
                    else:
                        self._codes[key].append(data)
                else:
                    self._codes[key] = [data]

    def _extractСodesFromTable(self, sh):
        destColumn, codeColumn, rateColumn, dateColumn, startLine, endLine = sh.dataFormat
        for line in range(startLine, endLine + 1):
            destination = sh.worksheet.cell(row=line, column=destColumn).value
            code = sh.worksheet.cell(row=line, column=codeColumn).value
            rate = sh.worksheet.cell(row=line, column=rateColumn).value

            if not self._checkEmptyLines(code, rate):
                break

            lineError = False
            if not self._codeIsValid(code):
                self._addError(sh, line, codeColumn)
                lineError = True
            if not self._rateIsValid(rate):
                self._addError(sh, line, rateColumn)
                lineError = True
            if not self._destinationIsValid(destination):
                self._addError(sh, line, destColumn)

            if not lineError:
                data = (str(sh), destination, rate, line)
                utilities.appendToMapsList(self._codes, int(code), data)


    def _checkEmptyLines(self, code, rate):
        if code is None and rate is None:
            self._skipLinesCounter += 1
            if self._skipLinesCounter == 15:
                return False
        else:
            self._skipLinesCounter = 0
        return True

    def _addError(self, sheet, line, column):
        self._clrErrors.append((sheet, line, column))

    def getErrors(self):
        return self._clrErrors

    def printCodes(self):
        i = 0
        for code in sorted(self._codes):
            if i % 100 == 0:
                print(f"{code}: {self._codes[code]}")
            i += 1

    def getResult(self):
        return self._codes

    def getFilenames(self):
        for sheet in self._parsedSheets:
            yield sheet.filename

    def getMaxCountOfSheetsForCode(self):
        return self._maxCountOfSheetsForCode

    def _clearErrors(self):
        self._clrErrors = []

    def _codeIsValid(self, code):
        return isinstance(code, int) or (isinstance(code, str) and code.isdigit())

    def _rateIsValid(self, rate):
        return (isinstance(rate, int) or isinstance(rate, float)) and rate >= 0

    def _destinationIsValid(self, destination):
        return destination != "" #isinstance(destination, str) and all(not char.isdigit() for char in destination)

    def removeSheet(self, sheet: Sheet):
        self._loadedSheets.remove(sheet)

    def removeAllSheets(self):
        self._loadedSheets.clear()

    # def removeAllSheetsExceptFiles(self, selectedFiles):
    #     if not self._loadedSheets:
    #         return
    #     oldSheets = self._loadedSheets
    #     self._loadedSheets = []
    #     for file in selectedFiles:
    #
    def removeAllSheetsExceptFiles(self, selectedFiles):
        self._loadedSheets = list(filter(lambda sheet: sheet.fullFilePath in selectedFiles, self._loadedSheets))

