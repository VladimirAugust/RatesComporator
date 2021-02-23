# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SheetErrorsWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.0.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_SheetErrorsWindow(object):
    def setupUi(self, SheetErrorsWindow):
        if not SheetErrorsWindow.objectName():
            SheetErrorsWindow.setObjectName(u"SheetErrorsWindow")
        SheetErrorsWindow.resize(800, 600)
        self.centralwidget = QWidget(SheetErrorsWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout.addWidget(self.tableWidget)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(150, 0))

        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        SheetErrorsWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(SheetErrorsWindow)

        QMetaObject.connectSlotsByName(SheetErrorsWindow)
    # setupUi

    def retranslateUi(self, SheetErrorsWindow):
        SheetErrorsWindow.setWindowTitle(QCoreApplication.translate("SheetErrorsWindow", u"Sheet errors", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("SheetErrorsWindow", u"File", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("SheetErrorsWindow", u"Sheet", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("SheetErrorsWindow", u"Row", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("SheetErrorsWindow", u"Column", None));
        self.pushButton.setText(QCoreApplication.translate("SheetErrorsWindow", u"Close", None))
    # retranslateUi

