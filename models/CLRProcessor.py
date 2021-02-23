from toolz.dicttoolz import valfilter

from models.utilities import appendToMapsList


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

    def setCodeFilter(self, codes: list):
        self._codesFilter = codes

    def clearCodeFilter(self):
        self._codesFilter = None

    def setRateFilter(self, rate):
        self._rateFilter = rate

    def clearRateFilter(self):
        self._rateFilter = None

    def buildCLR(self):
        self._clearErrors()
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
        if self._codesFilter.endswith('!'):
            filter =int(self._codesFilter[:-1])
            for key in self._codes.keys():
                if key == filter:
                    yield key
        else:
            for key in self._codes.keys():
                if str(key).startswith(self._codesFilter):
                    yield key

    def _loadSheetsData(self):
        self._codes = {}
        for sheet in self._loadedSheets:
            if not sheet.loaded:
                print(f"The sheet {sheet.fileName} was not loaded. Skipping")
                continue
            destColumn, codeColumn, rateColumn, startLine, endLine = sheet.dataFormat
            skipLines = 0
            for line in range(startLine, endLine + 1):
                destination = sheet.worksheet.cell(row=line, column=destColumn).value
                code = sheet.worksheet.cell(row=line, column=codeColumn).value
                rate = sheet.worksheet.cell(row=line, column=rateColumn).value
                # empty lines checking:
                if code is None and rate is None:
                    skipLines += 1
                    if skipLines == 15:
                        break
                else:
                    skipLines = 0
                    lineError = False
                    if not self._codeIsValid(code):
                        self._addError(sheet, line, codeColumn)
                        lineError = True
                    if not self._rateIsValid(rate):
                        self._addError(sheet, line, rateColumn)
                        lineError = True
                    if not self._destinationIsValid(destination):
                        self._addError(sheet, line, destColumn)
                    if not lineError:
                        appendToMapsList(self._codes, int(code), (str(sheet), destination, rate, line))

            self._parsedSheets.append(sheet)

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
        return isinstance(destination, str) and all(not char.isdigit() for char in destination)
