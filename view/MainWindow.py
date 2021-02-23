import ntpath
from os import path

from PySide6 import QtWidgets
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QMainWindow, QListWidgetItem, QFileDialog, QTableWidgetItem

from models.CLRThreadWorker import CLRThreadWorker
from models.DataRecognitionSystem import DataRecognitionSystem
from view.SetAliasesWindow import SetAliasesWindow
from view.SheetErrorsWindow import SheetErrorsWindow
from view.ui_MainWindow import Ui_MainWindow


class MainWindow(QMainWindow):
    _clrWorker = None

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # ui initialization:
        self.ui.clrTable.verticalHeader().setVisible(False)
        self.ui.clrTable.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.ui.stackedWidget.setCurrentIndex(0)
        self.setCLRErrorListVisible(False)
        self._setAliasesDialog = SetAliasesWindow(self)
        self._sheetErrorsWindow = SheetErrorsWindow()
        self.ui.page3ShowErrorsBtn.setVisible(False)

        # field initialization:
        self._dataRecognitionSystem = DataRecognitionSystem()
        self._clrWorker = CLRThreadWorker(self._dataRecognitionSystem)
        # self.selectedFiles = [('C:/Users/User/PycharmProjects/RatesComparator/data/7741_Airtime_Tech_RTX_Ratesheet_2020-12-11.xlsx', ''),
        #                       ('C:/Users/User/PycharmProjects/RatesComparator/data/Korea_Telecom_CLI_28082020.xlsx', ''),
        #                       ('C:/Users/User/PycharmProjects/RatesComparator/data/RouteTrader_EUR_CLI_04082020.xlsx', ''),
        #                       ('C:/Users/User/PycharmProjects/RatesComparator/data/Symbio_MVP_International_Standard_Rate_Card_B5F1120(1).xlsx', '')]
        # self.ui.page2NextBtn.setEnabled(True)
        self._selectedFiles = []

        self.linkActions()





    def linkActions(self):
        # Page 1:
        self.ui.page1NextBtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))

        # Page 2:
        self.ui.btnAddFiles.clicked.connect(self.addFiles)
        self.ui.filesList.selectionModel().selectionChanged.connect(self.filesListChanged)
        self.ui.btnDelFiles.clicked.connect(self.deleteSelectedFile)
        self.ui.page2BackBtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.page2NextBtn.clicked.connect(self.page2NextBtnClicked)

        # Page 3 (CLR):
        self.ui.page3SetAliasesBtn.clicked.connect(self.setAliases)
        self.ui.clrErrorslist.doubleClicked.connect(self.setAliases)
        self.ui.page3GoBackBtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.page3ShowErrorsBtn.clicked.connect(lambda: self._sheetErrorsWindow.show())

        # CLR Worker:
        self._clrWorker.updateClrStatusSignal.connect(self.changeCLRStatus)
        self._clrWorker.updateCLRTableWidgetSignal.connect(self.updateCLRTableWidget)
        self._clrWorker.addUndefinedSheetListSignal.connect(self.addUndefinedCLRsheet)
        self._clrWorker.clearUndefinedSheetListSignal.connect(self.clearUndefinedSheetList)
        self._clrWorker.updateSheetErrorsSignal.connect(self.updateSheetErrorsUI)


    @Slot()
    def clearUndefinedSheetList(self):
        self.ui.clrErrorslist.clear()
        self.setCLRErrorListVisible(False)

    @Slot()
    def setAliases(self):
        self._setAliasesDialog.exec_()
        if self._setAliasesDialog.isOk():
            values = self._setAliasesDialog.getValues()
            self._clrWorker.updateDataForUndefinedSheets(values)


    def setCLRErrorListVisible(self, visible:bool):
        self.ui.clrErrorLabel.setVisible(visible)
        self.ui.clrErrorslist.setVisible(visible)
        self.ui.page3SetAliasesBtn.setVisible(visible)

    @Slot()
    def addUndefinedCLRsheet(self, sheet):
        self.setCLRErrorListVisible(True)
        self.ui.clrErrorslist.addItem(QListWidgetItem(str(sheet.filename)))

    @Slot()
    def page2NextBtnClicked(self):
        self.ui.stackedWidget.setCurrentIndex(2)
        self._clrWorker.setFiles(self._selectedFiles)
        if self.ui.radioOpt1.isChecked():
            self._clrWorker.setWorkMode1()
        elif self.ui.radioOpt2.isChecked():
            self._clrWorker.setWorkMode2(self.ui.destEdit.text(), self.ui.codeEdit.text(), self.ui.rateEdit.text())
        self._clrWorker.start()
        # self._clrWorker.run()


    @Slot()
    def deleteSelectedFile(self):
        for i in self.ui.filesList.selectedItems():
            for f in self._selectedFiles:
                if f[1] == i.text():
                    self._selectedFiles.remove(f)
        # for i in self.selectedFiles:
        #     print(i)
        for i in self.ui.filesList.selectedItems():
            self.ui.filesList.takeItem(self.ui.filesList.row(i))
        self.ui.page2NextBtn.setEnabled(len(self._selectedFiles) > 0)

    @Slot()
    def filesListChanged(self):
        self.ui.btnDelFiles.setEnabled(len(self.ui.filesList.selectedItems()) > 0)

    @Slot()
    def addFiles(self):
        files = QFileDialog.getOpenFileNames(self, "Add file", "", "Excel Files (*.xlsx *.xlsm *.xltx *.xltm);;All files (*.*)")
        for f in files[0]:
            head, tail = ntpath.split(f)
            caption = f"{tail} \t({head})"
            widgetItem = (f, caption)
            if widgetItem not in self._selectedFiles:
                self._selectedFiles.append(widgetItem)
                self.ui.filesList.addItem(caption)
        if len(self._selectedFiles) > 0:
            self.ui.page2NextBtn.setEnabled(True)



    def enableFields(self, enabled=True):
        self.ui.destlabel.setEnabled(enabled)
        self.ui.codeLabel.setEnabled(enabled)
        self.ui.rateLabel.setEnabled(enabled)
        self.ui.destEdit.setEnabled(enabled)
        self.ui.codeEdit.setEnabled(enabled)
        self.ui.rateEdit.setEnabled(enabled)

    @Slot()
    def changeCLRStatus(self, text):
        self.ui.statusbar.showMessage(text)

    @Slot()
    def updateCLRTableWidget(self, signal):
        clr = self._clrWorker.getCLR()
        table = self.ui.clrTable
        table.clear()
        table.setColumnCount(3)
        table.setHorizontalHeaderLabels(["Destination", "Codes", "Least cost"])
        table.setRowCount(1)
        table.setSpan(0, 0, 1, 1)
        if signal == 0:
            return
        codes = clr.getResult()
        if len(codes) == 0:
            table.setItem(0, 0, QTableWidgetItem("No data found"))
            table.setSpan(0, 0, 1, 3)
            return
        maxc = clr.getMaxCountOfSheetsForCode()
        colNames = ["Destination", "Codes", "Least cost"] + ["Next least cost" for i in range(1*(maxc-1))]
        table.setColumnCount(2 + maxc)
        table.setHorizontalHeaderLabels(colNames)
        table.setRowCount(len(codes))
        m = 0
        prevCountryName = ""
        for i, code in enumerate(sorted(codes)):
            countryName = str(codes[code][0][1])
            if countryName == prevCountryName:
                m += 1
                #print(i, code, i - m, 0, 1, m+1)
                table.setSpan(i - m, 0, m+1, 1)
            else:
                m = 0
                table.setItem(i, 0, QTableWidgetItem(countryName))
            table.setItem(i, 1, QTableWidgetItem(str(code)))
            cc = len(codes[code])
            for j in range(cc):
                filename = str(codes[code][j][0])
                price = "{:.2f}".format(codes[code][j][2])
                table.setItem(i, 2 + j, QTableWidgetItem(f"({price}) {filename}"))
            prevCountryName = countryName
            #if i == 0: break

        table.resizeColumnsToContents()

    def updateSheetErrorsUI(self, data):
        self.ui.page3ShowErrorsBtn.setVisible(len(data) > 0)
        self._sheetErrorsWindow.setErrors(data)
