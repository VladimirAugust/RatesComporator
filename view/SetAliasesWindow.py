from PySide6 import QtWidgets

from view.ui_SetAliasDialog import Ui_SetAliasDialog


class SetAliasesWindow(QtWidgets.QDialog):
    def __init__(self, parent):
        super(SetAliasesWindow, self).__init__(parent)
        self.ui = Ui_SetAliasDialog()
        self.ui.setupUi(self)

        self._isOk = False


    def accept(self):
        if self.ui.destAlias.text() and self.ui.codeAlias.text() and self.ui.rateAlias.text():
            self._isOk = True
            self.close()
        else:
            self.ui.errorLabel.setText("Please fill in all fields")

    def reject(self):
        self.close()

    def closeEvent(self, event):
        event.accept()

    def isOk(self):
        return self._isOk

    def getValues(self):
        return self.ui.destAlias.text(), self.ui.codeAlias.text(), self.ui.rateAlias.text()