import ntpath
from os import path

from PySide6 import QtWidgets
from PySide6.QtCore import Slot, QRegularExpression
from PySide6.QtGui import QValidator, QRegularExpressionValidator
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
        self.setUndefinedSheetsListVisible(False)
        self._setAliasesDialog = SetAliasesWindow(self)
        self._sheetErrorsWindow = SheetErrorsWindow()
        self.ui.page3ShowErrorsBtn.setVisible(False)

        #self.ui.clrTable.setStyleSheet("QTableWidget::section{border-width: 1px; border-color: #BABABA; border-style:solid;}")
        ##self.ui.clrTable.setStyleSheet("table.grid-all>*>tr>.tableblock:last-child,table.grid-cols>*>tr>.tableblock:last-child{border-right-width:1}")
        # table.grid - all
        # {
        #     border - collapse: collapse;
        # }
        # https://discuss.asciidoctor.org/Bug-loss-of-borders-in-table-when-span-cells-is-used-td7382.html

        # field initialization:
        self._dataRecognitionSystem = DataRecognitionSystem()
        self._dataRecognitionSystem.loadUserAliasesFromFile(DataRecognitionSystem.USERALIASES_STANDARD_FILE)
        self._clrWorker = CLRThreadWorker(self._dataRecognitionSystem)
        self._selectedFiles = []

        self.linkActions()





    def linkActions(self):
        # Page 1:
        self.ui.page1NextBtn.clicked.connect(self._page1NextBtnAction)
        self.ui.codeEdit.setValidator(QRegularExpressionValidator(QRegularExpression("[0-9]+[!]?")));
        self.ui.rateEdit.setValidator(QRegularExpressionValidator(QRegularExpression("[0-9]+\\.[0-9]*")));

        # Page 2:
        self.ui.btnAddFiles.clicked.connect(self.addFiles)
        self.ui.filesList.selectionModel().selectionChanged.connect(self.filesListSelectionChanged)
        self.ui.btnDelFiles.clicked.connect(self.deleteSelectedFile)
        self.ui.p2DellAllBtn.clicked.connect(self.deleteAllFiles)
        self.ui.page2BackBtn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.page2NextBtn.clicked.connect(self.page2NextBtnClicked)

        # Page 3 (CLR):
        self.ui.page3SetAliasesBtn.clicked.connect(self.setAliases)
        self.ui.clrUndefSheetslist.doubleClicked.connect(self.setAliases)
        self.ui.page3GoBackBtn.clicked.connect(self.page3BackBtnAction)
        self.ui.page3ShowErrorsBtn.clicked.connect(lambda: self._sheetErrorsWindow.show())

        # CLR Worker:
        self._clrWorker.updateClrStatusSignal.connect(self.changeCLRStatus)
        self._clrWorker.updateCLRTableWidgetSignal.connect(self.updateCLRTableWidget)
        self._clrWorker.addUndefinedSheetListSignal.connect(self.addUndefinedCLRsheet)
        self._clrWorker.clearUndefinedSheetListSignal.connect(self.clearUndefinedSheetList)
        self._clrWorker.updateSheetErrorsSignal.connect(self.updateSheetErrorsUI)


    @Slot()
    def page3BackBtnAction(self):
        self.ui.stackedWidget.setCurrentIndex(0)
        self.clearUndefinedSheetList()
        self.ui.statusbar.clearMessage()

    @Slot()
    def _page1NextBtnAction(self):
        if self.ui.radioOpt2.isChecked():
            dest = self.ui.destEdit.text()
            code = self.ui.codeEdit.text()
            rate = self.ui.rateEdit.text()
            if (not dest or dest.isspace()) and not rate and not code:
                return
        self.ui.stackedWidget.setCurrentIndex(1)

    @Slot()
    def clearUndefinedSheetList(self):
        self.ui.clrUndefSheetslist.clear()
        self.setUndefinedSheetsListVisible(False)

    @Slot()
    def setAliases(self):
        aliases = self._dataRecognitionSystem.getUserAliases()
        self._setAliasesDialog.setAliases(aliases)
        self._setAliasesDialog.exec_()
        if self._setAliasesDialog.isOk():
            values = self._setAliasesDialog.getValues()
            self._clrWorker.updateDataForUndefinedSheets(values)



    def setUndefinedSheetsListVisible(self, visible:bool):
        self.ui.clrErrorLabel.setVisible(visible)
        self.ui.clrUndefSheetslist.setVisible(visible)
        self.ui.page3SetAliasesBtn.setVisible(visible)

    @Slot()
    def addUndefinedCLRsheet(self, sheet):
        self.setUndefinedSheetsListVisible(True)
        self.ui.clrUndefSheetslist.addItem(QListWidgetItem(str(sheet.filename)))

    @Slot()
    def page2NextBtnClicked(self):
        self.ui.stackedWidget.setCurrentIndex(2)
        self._clrWorker.setFiles([f[0] for f in self._selectedFiles])
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
        for i in self.ui.filesList.selectedItems():
            self.ui.filesList.takeItem(self.ui.filesList.row(i))
        self.ui.page2NextBtn.setEnabled(len(self._selectedFiles) > 0)

    @Slot()
    def deleteAllFiles(self):
        self._selectedFiles.clear()
        self.ui.filesList.clear()
        self.ui.btnDelFiles.setEnabled(False)
        self.ui.p2DellAllBtn.setEnabled(False)
        self.ui.page2NextBtn.setEnabled(False)

    @Slot()
    def filesListSelectionChanged(self):
        self.ui.btnDelFiles.setEnabled(len(self.ui.filesList.selectedItems()) > 0)
        self.ui.p2DellAllBtn.setEnabled(self.ui.filesList.count() > 0)

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
            self.ui.p2DellAllBtn.setEnabled(True)



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
        colNames = ["Destination", "Codes", "Least cost"] + [self._generateColumnName(i+2) for i in range(maxc-1)]
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
                price = "{:.5f}".format(codes[code][j][2])
                table.setItem(i, 2 + j, QTableWidgetItem(f"({price}) {filename}"))
            prevCountryName = countryName
            #if i == 0: break

        table.resizeColumnsToContents()

    def updateSheetErrorsUI(self, data):
        self.ui.page3ShowErrorsBtn.setVisible(len(data) > 0)
        self._sheetErrorsWindow.setErrors(data)

    def _generateColumnName(self, i):
        assert i >= 2, "i should be >= 2"
        if i == 2:
            return "2nd least cost"
        elif i == 3:
            return "3rd least cost"
        else:
            return f"{i}th least cost"
