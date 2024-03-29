import json
from builtins import FileNotFoundError

from models.Sheet import Sheet


class DataRecognitionSystem:
    USERALIASES_STANDARD_FILE = "aliases.json"
    countryAliases = ["destination", "country"]
    codeAliases = ["prefix", "dial", "code"]
    rateAliases = ["rate", "current rate", "price"]
    dateAliases = ["date"]
    userCountryAliases = []
    userCodeAliases = []
    userRateAliases = []

    def determineSheetData(self, sheet: Sheet):
        for sheetname in sheet.workbook.sheetnames:
            worksheet = sheet.workbook[sheetname]
            for line in range(1, 71):
                destCol = self.findAlias(line, self.countryAliases + self.userCountryAliases, worksheet)
                codeCol = self.findAlias(line, self.codeAliases + self.userCodeAliases, worksheet, [destCol])
                rateCol = self.findAlias(line, self.rateAliases + self.userRateAliases, worksheet, [destCol, codeCol])
                dateCol = self.findAlias(line, self.dateAliases, worksheet, [destCol, codeCol, rateCol])

                if destCol > 0 and codeCol > 0 and rateCol > 0:
                    dataLine = self.findDataRow(line, rateCol, worksheet)
                    if dataLine != -1:
                        sheet.setDataFormat(sheetname, destCol, codeCol, rateCol, dateCol, dataLine)
                        break

    def setUserAliases(self, userAliases):
        assert len(userAliases) == 3, 'userAliases len should be = 3'
        userAliases = list(userAliases)
        for i in range(len(userAliases)):
            userAliases[i] = userAliases[i].split(",")
            for j in range(len(userAliases[i])):
                userAliases[i][j] = userAliases[i][j].strip().lower()

        for aliasCat in userAliases:
            for alias in aliasCat:
                if alias == '' or alias.isspace():
                    aliasCat.remove(alias)

        self.userCountryAliases = userAliases[0]
        self.userCodeAliases = userAliases[1]
        self.userRateAliases = userAliases[2]
        self.saveUserAliasesToFile(self.USERALIASES_STANDARD_FILE)
        print(f"Updated user aliases: ", self.userCountryAliases, self.userCodeAliases, self.userRateAliases)

    def saveUserAliasesToFile(self, filename):
        out = {
            "country_aliases": self.userCountryAliases,
            "code_aliases": self.userCodeAliases,
            "rate_aliases": self.userRateAliases
        }
        try:
            with open(filename, "w", encoding='utf-8') as f:
                json.dump(out, f)
                print("The new aliases was successfully saved to file")
        except IOError as e:
            print("Couldn't save user aliases:", e)

    def loadUserAliasesFromFile(self, filename):
        try:
            with open(filename, "r") as f:
                data = json.load(f)
                self.userCountryAliases = data['country_aliases']
                self.userCodeAliases = data['code_aliases']
                self.userRateAliases = data['rate_aliases']
        except (KeyError, FileNotFoundError, IOError) as e:
            print("Couldn't load user aliases:", e)

    def getUserAliases(self):
        return self.userCountryAliases, self.userCodeAliases, self.userRateAliases

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
                    # print(f"Found = {alias} in the cell {line}-{column} ({cellValue})")
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
                        # print(f"Found 'in' {alias} in the cell {line}-{column} ({cellValue})")
                        break
        return resColumn

    def findDataRow(self, headersLine, rateColumn, worksheet):
        for line in range(headersLine + 1, headersLine + 10):
            cellValue = worksheet.cell(row=line, column=rateColumn).value
            if type(cellValue) == float or type(cellValue) == int:
                return line
        return -1
