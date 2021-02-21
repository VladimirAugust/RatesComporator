from os import path

from PySide6 import QtCore

from models.CLRProcessor import CLRProcessor
from models.DataRecognitionSystem import DataRecognitionSystem
from models.Sheet import Sheet


class CLRWorker(QtCore.QThread):
    updateClrStatusSignal = QtCore.Signal(str)
    updateTableWidgetSignal = QtCore.Signal(int)
    addUndefinedSheetListSignal = QtCore.Signal(Sheet)
    clearUndefinedSheetListSignal = QtCore.Signal()

    def __init__(self, dataRecognitionSystem : DataRecognitionSystem):
        QtCore.QThread.__init__(self)
        self._clr = CLRProcessor()
        self._dataRecognitionSystem = dataRecognitionSystem
        self._selectedFiles = None
        self._undefinedSheets = []


    def setFiles(self, files):
        self._selectedFiles = files

    def updateDataForUndefinedSheet(self, sheetNum, data):
        sheet = self._undefinedSheets[sheetNum]
        self._dataRecognitionSystem.determineSheetData(sheet, data)
        if not sheet.isDataFormatDefined():
            self.updateClrStatusSignal.emit(f"Could not define columns for the specified aliases in the sheet {sheet.filename}")
        else:
            self._undefinedSheets.remove(sheet)
            self._clr.addSheet(sheet)
            self._clr.buildCLR()
            self.updateTableWidgetSignal.emit(1)
            self.updateClrStatusSignal.emit(f"Column definition succeeded for the sheet {sheet.filename}. CLR Table was rebuilt")
            self._updateUndefinedSheetList()

    def run(self):
        for file in self._selectedFiles:
            self.updateClrStatusSignal.emit(f"Loading file {ntpath.basename(file[0])}...")
            sheet = Sheet(file[0])
            sheet.load()
            self._dataRecognitionSystem.determineSheetData(sheet)
            sheet.printInfo()
            if not sheet.isDataFormatDefined():
                print("Coudn't define data in the sheet ", sheet)
                self._undefinedSheets.append(sheet)
            else:
                self._clr.addSheet(sheet)

        self._updateUndefinedSheetList()
        self.updateClrStatusSignal.emit("Parsing data...")
        #st = time.time()
        self._clr.buildCLR()
        #print("@", time.time() - st)
        self.updateClrStatusSignal.emit("Populating result table...")
        self.updateTableWidgetSignal.emit(1)
        #self.clr.printCodes()
        if len(self._undefinedSheets) == 0:
            self.updateClrStatusSignal.emit("Done. All sheets were parsed successfully")
        else:
            self.updateClrStatusSignal.emit("Done. Please set manually aliases for unparsed sheets")

    def _updateUndefinedSheetList(self):
        self.clearUndefinedSheetListSignal.emit()
        for sheet in self._undefinedSheets:
            self.addUndefinedSheetListSignal.emit(sheet)

    def getCLR(self):
        return self._clr

    def getUndefinedSheetSheetnames(self, num):
        return self._undefinedSheets[num].sheetnames