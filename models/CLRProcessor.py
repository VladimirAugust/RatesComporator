import ntpath

from models.comp_functions import appendToMapsList


class CLRProcessor:
    def __init__(self):
        self._loadedSheets = []
        self._parsedSheets = []
        self._codes = {}
        self._complete = False
        self._maxCountOfSheetsForCode = 1

    def addSheet(self, sheet):
        self._loadedSheets.append(sheet)

    def buildCLR(self):
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
                if destination is None or code is None or rate is None:
                    #print(f"!!! CLR skipping {sheet} at line {line}")
                    skipLines += 1
                    if skipLines == 15:
                        break
                else:
                    skipLines = 0
                    appendToMapsList(self._codes, int(code), (str(sheet), destination, rate, line))


            self._parsedSheets.append(sheet)

        for code in self._codes:
            if len(self._codes[code]) > 1:
                sortedList = sorted(self._codes[code], key=lambda x: x[2])
                #print("Old ", code, self._codes[code])
                #print("New ", code, sortedList)
                self._codes[code] = sortedList
                if len(self._codes[code]) > self._maxCountOfSheetsForCode:
                    self._maxCountOfSheetsForCode = len(self._codes[code])
        self._complete = True

    def printCodes(self):
        i = 0
        for code in sorted(self._codes):
            if i % 100 == 0:
                print(f"{code}: {self._codes[code]}")
            i += 1

    @property
    def complete(self):
        return self._complete

    def getAllCodes(self):
        return self._codes

    def getFilenames(self):
        for sheet in self._parsedSheets:
            yield sheet.filename

    def getMaxCountOfSheetsForCode(self):
        return self._maxCountOfSheetsForCode
