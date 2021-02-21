
def appendToMapsList(map, key, data):
    if key in map:
        map[key].append(data)
    else:
        map[key] = [data]


def findByDestination(sheetInfo, searchStr, caseSensitive=False):
    results = {}
    destinationColumn = sheetInfo.destColumn
    codeColumn = sheetInfo.codeColumn
    rateColumn = sheetInfo.rateColumn
    startLine = sheetInfo.startLine
    sheet = sheetInfo.worksheet
    for line in range(startLine, sheet.max_row + 1):
        destination = sheet.cell(row=line, column=destinationColumn).value
        code = sheet.cell(row=line, column=codeColumn).value
        rate = sheet.cell(row=line, column=rateColumn).value
        if caseSensitive and searchStr in destination:
            appendToMapsList(results, destination, (code, rate))
        elif not caseSensitive and searchStr.lower() in destination.lower():
            appendToMapsList(results, destination, (code, rate))
    return results


def findByCode(sheetInfo, searchStr):
    results = {}
    searchStr = str(searchStr)
    destinationColumn = sheetInfo.destColumn
    codeColumn = sheetInfo.codeColumn
    rateColumn = sheetInfo.rateColumn
    startLine = sheetInfo.startLine
    sheet = sheetInfo.worksheet
    for line in range(startLine, sheet.max_row + 1):
        destination = sheet.cell(row=line, column=destinationColumn).value
        code = sheet.cell(row=line, column=codeColumn).value
        rate = sheet.cell(row=line, column=rateColumn).value
        if searchStr == code:
            if destination in results:
                results[destination].append((code, rate))
            else:
                results[destination] = [(code, rate)]
    return results


def printResults(results):
    for c in results:
        print(c, ":")
        print(results[c])

# timeStart = time.time()
# wb1 = load_workbook('data/7741_Airtime_Tech_RTX_Ratesheet_2020-12-11.xlsx')
# print("File opening took %.4f sec" % (time.time() - timeStart))
# timeStart = time.time()
# wb2 = load_workbook('data/Korea_Telecom_CLI_28082020.xlsx')
# print("File opening took %.4f sec" % (time.time() - timeStart))
# timeStart = time.time()
# wb3 = load_workbook('data/Symbio_MVP_International_Standard_Rate_Card_B5F1120(1).xlsx')
# print("File opening took %.4f sec" % (time.time() - timeStart))
#
# sheet1 = SheetInformation(wb1, wb1.worksheets[0], 11, 'A', 'B', 'C')
# sheet2 = SheetInformation(wb2, wb2.worksheets[0], 8, 'A', 'H', 'C')
# sheet3 = SheetInformation(wb3, wb3['Rates'], 11, 'A', 'B', 'C')
#
#
#
# timeStart = time.time()
#
#
# printResults(findByCode(sheet1, 21365))
#
# print("=" * 30)
#
# results = findByDestination(sheet2, "Albania", False)
# for c in results:
#     print(c, ":")
#     print(results[c])
# print("=" * 30)
# results = findByDestination(sheet3, "Albania", False)
# for c in results:
#     print(c, ":")
#     print(results[c])
# print("=" * 30)
#
# print("The search took %.4f sec" % (time.time() - timeStart))
