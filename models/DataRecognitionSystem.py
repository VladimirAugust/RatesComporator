import time

from models.Sheet import Sheet


class DataRecognitionSystem:
    countryNames = ["destination", "country"]
    codeNames = ["prefix", "dial", "code"]
    rateNames = ["rate", "current rate", "price"]

    def determineSheetData(self, sheet: Sheet, extraAliases = []):
        if extraAliases:
            assert len(extraAliases) == 3, 'extraAliases len should be = 3'
            self.updateAliases(extraAliases)
        #print("Working with sheet ", sheet)

        for sheetname in sheet.workbook.sheetnames:
            worksheet = sheet.workbook[sheetname]
            #print("Working with sheet ", sheetname)

            for line in range(1, 71):
                # if line == 6 and "Korea" in str(sheet):
                #     print("!")
                # if line == 10 and "Airtime" in str(sheet):
                #     print("!")

                destCol = self.findAlias(line, self.countryNames, worksheet)
                codeCol = self.findAlias(line, self.codeNames, worksheet, [destCol])
                rateCol = self.findAlias(line, self.rateNames, worksheet, [destCol, codeCol])

                if destCol > 0 and codeCol > 0 and rateCol > 0:
                    #print(f"Search finished on sheet {sheetname}")
                    #print(f"Found dest:{destCol}    code:{codeCol}  rate:{rateCol} on the line {line}")
                    dataLine = self.findDataRow(line, rateCol, worksheet)
                    if dataLine != -1:
                        #print(f"Found data line {dataLine}")
                        sheet.setDataFormat(sheetname, destCol, codeCol, rateCol, dataLine)
                        break

    def updateAliases(self, extraAliases):
        extraAliases = list(extraAliases)
        for i in range(len(extraAliases)):
            extraAliases[i] = extraAliases[i].split(",")
            for j in range(len(extraAliases[i])):
                extraAliases[i][j] = extraAliases[i][j].strip().lower()
        self.countryNames.extend(extraAliases[0])
        self.codeNames.extend(extraAliases[1])
        self.rateNames.extend(extraAliases[2])

    def findAlias(self, line, array, worksheet, ignoreColumns=[]):
        resColumn = 0
        for alias in array:
            for column in range(1, 21):
                if column in ignoreColumns:
                    continue
                cellValue = worksheet.cell(row=line, column=column).value
                if type(cellValue) != str:
                    continue
                if cellValue.lower() == alias:
                    resColumn = column
                    #print(f"Found = {alias} in the cell {line}-{column} ({cellValue})")
                    break
            if resColumn == 0:
                for column in range(1, 21):
                    if column in ignoreColumns:
                        continue
                    cellValue = worksheet.cell(row=line, column=column).value
                    if type(cellValue) != str:
                        continue
                    if alias in cellValue.lower():
                        resColumn = column
                        #print(f"Found 'in' {alias} in the cell {line}-{column} ({cellValue})")
                        break
        return resColumn

    def findDataRow(self, headersLine, rateColumn, worksheet):
        for line in range(headersLine + 1, headersLine + 10):
            cellValue = worksheet.cell(row=line, column=rateColumn).value
            if type(cellValue) == float or type(cellValue) == int:
                return line
        return -1
