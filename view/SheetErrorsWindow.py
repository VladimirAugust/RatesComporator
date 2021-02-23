from PySide6 import QtWidgets
from PySide6.QtWidgets import QTableWidgetItem, QHeaderView

from view.ui_SheetErrorsWindow import Ui_SheetErrorsWindow


class SheetErrorsWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(SheetErrorsWindow, self).__init__()
        self.ui = Ui_SheetErrorsWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.close)

    def setErrors(self, errors: list):
        table = self.ui.tableWidget
        table.clear()
        table.setRowCount(len(errors))
        table.setHorizontalHeaderLabels(["File", "Sheet", "Row", "Column"])
        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        table.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        for i, error in enumerate(errors):
            sheet = error[0]
            table.setItem(i, 0, QTableWidgetItem(sheet.filename))
            table.setItem(i, 1, QTableWidgetItem(str(sheet.worksheet.title)))
            table.setItem(i, 2, QTableWidgetItem(str(error[1])))
            table.setItem(i, 3, QTableWidgetItem(str(error[2])))
        # table.resizeColumnsToContents()

