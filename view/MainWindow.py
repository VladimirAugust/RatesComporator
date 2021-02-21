from os import path

from PySide6 import QtWidgets
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QMainWindow, QListWidgetItem, QFileDialog, QTableWidgetItem

from models.CLRWorker import CLRWorker
from models.DataRecognitionSystem import DataRecognitionSystem
from view.SetAliasesWindow import SetAliasesWindow
from view.ui_MainWindow import Ui_MainWindow


class MainWindow(QMainWindow):
    _clrWorker = None

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.clrTable.verticalHeader().setVisible(False)
        self.ui.clrTable.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.ui.stackedWidget.setCurrentIndex(0)
        self.setCLRErrorListVisible(False)

        self._dataRecognitionSystem = DataRecognitionSystem()
        self._clrWorker = CLRWorker(self._dataRecognitionSystem)
        # self.selectedFiles = [('C:/Users/User/PycharmProjects/RatesComparator/data/7741_Airtime_Tech_RTX_Ratesheet_2020-12-11.xlsx', ''),
        #                       ('C:/Users/User/PycharmProjects/RatesComparator/data/Korea_Telecom_CLI_28082020.xlsx', ''),
        #                       ('C:/Users/User/PycharmProjects/RatesComparator/data/RouteTrader_EUR_CLI_04082020.xlsx', ''),
        #                       ('C:/Users/User/PycharmProjects/RatesComparator/data/Symbio_MVP_International_Standard_Rate_Card_B5F1120(1).xlsx', '')]
        # self.ui.page2NextBtn.setEnabled(True)
        self.selectedFiles = []

        self.linkActions()


    def linkActions(self):
        # Page 1:
        self.ui.page1NextBtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))

        # Page 2:
        self.ui.btnAddFiles.clicked.connect(self.addFiles)
        self.ui.filesList.selectionModel().selectionChanged.connect(self.filesListChanged)
        self.ui.btnDelFiles.clicked.connect(self.deleteSelectedFile)
        self.ui.page2NextBtn.clicked.connect(self.page2NextBtnClicked)

        # Page 3:
        self.ui.clrSetAlias.clicked.connect(self.setAliasForSheet)
        self.ui.clrErrorslist.doubleClicked.connect(self.setAliasForSheet)

        # CLR Worker:
        self._clrWorker.updateClrStatusSignal.connect(self.changeCLRStatus)
        self._clrWorker.updateTableWidgetSignal.connect(self.updateCLRTableWidget)
        self._clrWorker.addUndefinedSheetListSignal.connect(self.addUndefinedCLRsheet)
        self._clrWorker.clearUndefinedSheetListSignal.connect(self.clearUndefinedSheetList)

    @Slot()
    def clearUndefinedSheetList(self):
        self.ui.clrErrorslist.clear()
        self.setCLRErrorListVisible(False)

    @Slot()
    def setAliasForSheet(self):
        errorslist = self.ui.clrErrorslist
        items = errorslist.selectedItems()
        if not items:
            return
        itemNum = errorslist.row(items[0])

        dialog = SetAliasesWindow(self)
        dialog.exec_()
        if dialog.isOk():
            values = dialog.getValues()
            self._clrWorker.updateDataForUndefinedSheet(itemNum, values)


    def setCLRErrorListVisible(self, visible:bool):
        self.ui.clrErrorLabel.setVisible(visible)
        self.ui.clrErrorslist.setVisible(visible)
        self.ui.clrSetAlias.setVisible(visible)

    @Slot()
    def addUndefinedCLRsheet(self, sheet):
        self.setCLRErrorListVisible(True)
        self.ui.clrErrorslist.addItem(QListWidgetItem(str(sheet.filename)))

    @Slot()
    def page2NextBtnClicked(self):
        self.ui.stackedWidget.setCurrentIndex(2)
        self._clrWorker.setFiles(self.selectedFiles)
        self._clrWorker.start()
        #self._clrWorker.run()


    @Slot()
    def deleteSelectedFile(self):
        for i in self.ui.filesList.selectedItems():
            for f in self.selectedFiles:
                if f[1] == i.text():
                    self.selectedFiles.remove(f)
        # for i in self.selectedFiles:
        #     print(i)
        for i in self.ui.filesList.selectedItems():
            self.ui.filesList.takeItem(self.ui.filesList.row(i))
        self.ui.btnNext.setEnabled(len(self.selectedFiles) > 0)

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
            if widgetItem not in self.selectedFiles:
                self.selectedFiles.append(widgetItem)
                self.ui.filesList.addItem(caption)
        if len(self.selectedFiles) > 0:
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
    def updateCLRTableWidget(self):
        clr = self._clrWorker.getCLR()
        table = self.ui.clrTable

        if clr.complete:
            table.clear()
            codes = clr.getAllCodes()
            maxc = clr.getMaxCountOfSheetsForCode()
            colNames = ["Destination", "Codes", "Least cost"] + ["Next least cost" if True else "File" for i in range(1*(maxc-1))]
            table.setColumnCount(2 + 1*maxc)
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
                    # if code==51: print(codes[code][j])
                    filename = str(codes[code][j][0])
                    price = "{:.2f}".format(codes[code][j][2])
                    # table.setItem(i, 2 + j*2, QTableWidgetItem(price))
                    table.setItem(i, 2 + j, QTableWidgetItem(f"({price}) {filename}"))
                prevCountryName = countryName
                #if i == 0: break

            table.resizeColumnsToContents()