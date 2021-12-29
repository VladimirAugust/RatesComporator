# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.0.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(943, 715)
        MainWindow.setWindowOpacity(1.000000000000000)
        MainWindow.setStyleSheet(u"QRadioButton {\n"
"	margin-left: 50px;\n"
"	height: 60px;\n"
"}\n"
"QRadioButton#radioButton {\n"
"	margin-top: 20px;\n"
"}\n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.verticalLayout_2 = QVBoxLayout(self.page_1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.radioOpt1 = QRadioButton(self.page_1)
        self.radioOpt1.setObjectName(u"radioOpt1")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioOpt1.sizePolicy().hasHeightForWidth())
        self.radioOpt1.setSizePolicy(sizePolicy)
        self.radioOpt1.setSizeIncrement(QSize(0, 0))
        self.radioOpt1.setChecked(True)

        self.verticalLayout_2.addWidget(self.radioOpt1)

        self.radioOpt2 = QRadioButton(self.page_1)
        self.radioOpt2.setObjectName(u"radioOpt2")

        self.verticalLayout_2.addWidget(self.radioOpt2)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(50, 0, 60, 15)
        self.destlabel = QLabel(self.page_1)
        self.destlabel.setObjectName(u"destlabel")
        self.destlabel.setEnabled(False)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.destlabel)

        self.destEdit = QLineEdit(self.page_1)
        self.destEdit.setObjectName(u"destEdit")
        self.destEdit.setEnabled(False)
        self.destEdit.setMaxLength(32767)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.destEdit)

        self.codeLabel = QLabel(self.page_1)
        self.codeLabel.setObjectName(u"codeLabel")
        self.codeLabel.setEnabled(False)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.codeLabel)

        self.codeEdit = QLineEdit(self.page_1)
        self.codeEdit.setObjectName(u"codeEdit")
        self.codeEdit.setEnabled(False)
        self.codeEdit.setMaxLength(32767)
        self.codeEdit.setCursorPosition(0)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.codeEdit)

        self.rateLabel = QLabel(self.page_1)
        self.rateLabel.setObjectName(u"rateLabel")
        self.rateLabel.setEnabled(False)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.rateLabel)

        self.rateEdit = QLineEdit(self.page_1)
        self.rateEdit.setObjectName(u"rateEdit")
        self.rateEdit.setEnabled(False)
        self.rateEdit.setMaxLength(32767)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.rateEdit)


        self.verticalLayout_2.addLayout(self.formLayout)

        self.radioButton = QRadioButton(self.page_1)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setEnabled(False)

        self.verticalLayout_2.addWidget(self.radioButton)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_2.setContentsMargins(-1, -1, 0, -1)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.page1NextBtn = QPushButton(self.page_1)
        self.page1NextBtn.setObjectName(u"page1NextBtn")
        self.page1NextBtn.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_2.addWidget(self.page1NextBtn)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_3 = QVBoxLayout(self.page_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.page_2)
        self.label.setObjectName(u"label")

        self.verticalLayout_3.addWidget(self.label)

        self.filesList = QListWidget(self.page_2)
        self.filesList.setObjectName(u"filesList")
        self.filesList.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.filesList.setSortingEnabled(False)

        self.verticalLayout_3.addWidget(self.filesList)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, 0, -1, -1)
        self.p2DellAllBtn = QPushButton(self.page_2)
        self.p2DellAllBtn.setObjectName(u"p2DellAllBtn")
        self.p2DellAllBtn.setEnabled(False)
        self.p2DellAllBtn.setMinimumSize(QSize(150, 0))

        self.gridLayout.addWidget(self.p2DellAllBtn, 1, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 0, 1, 1)

        self.page2NextBtn = QPushButton(self.page_2)
        self.page2NextBtn.setObjectName(u"page2NextBtn")
        self.page2NextBtn.setEnabled(False)
        self.page2NextBtn.setMinimumSize(QSize(150, 0))

        self.gridLayout.addWidget(self.page2NextBtn, 1, 3, 1, 1)

        self.btnAddFiles = QPushButton(self.page_2)
        self.btnAddFiles.setObjectName(u"btnAddFiles")
        self.btnAddFiles.setMinimumSize(QSize(0, 0))

        self.gridLayout.addWidget(self.btnAddFiles, 0, 3, 1, 1)

        self.btnDelFiles = QPushButton(self.page_2)
        self.btnDelFiles.setObjectName(u"btnDelFiles")
        self.btnDelFiles.setEnabled(False)
        self.btnDelFiles.setMinimumSize(QSize(0, 0))

        self.gridLayout.addWidget(self.btnDelFiles, 0, 2, 1, 1)

        self.page2BackBtn = QPushButton(self.page_2)
        self.page2BackBtn.setObjectName(u"page2BackBtn")
        self.page2BackBtn.setMinimumSize(QSize(150, 0))

        self.gridLayout.addWidget(self.page2BackBtn, 1, 1, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_4 = QVBoxLayout(self.page_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.clrTable = QTableWidget(self.page_3)
        if (self.clrTable.columnCount() < 3):
            self.clrTable.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.clrTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.clrTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.clrTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.clrTable.setObjectName(u"clrTable")

        self.verticalLayout_4.addWidget(self.clrTable)

        self.clrErrorLabel = QLabel(self.page_3)
        self.clrErrorLabel.setObjectName(u"clrErrorLabel")

        self.verticalLayout_4.addWidget(self.clrErrorLabel)

        self.clrErrors = QHBoxLayout()
        self.clrErrors.setObjectName(u"clrErrors")
        self.clrErrors.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.clrErrorsSheetList = QListWidget(self.page_3)
        self.clrErrorsSheetList.setObjectName(u"clrErrorsSheetList")
        self.clrErrorsSheetList.setMaximumSize(QSize(16777215, 80))

        self.clrErrors.addWidget(self.clrErrorsSheetList, 0, Qt.AlignTop)


        self.verticalLayout_4.addLayout(self.clrErrors)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.page3GoBackBtn = QPushButton(self.page_3)
        self.page3GoBackBtn.setObjectName(u"page3GoBackBtn")
        self.page3GoBackBtn.setMinimumSize(QSize(152, 0))

        self.gridLayout_4.addWidget(self.page3GoBackBtn, 0, 0, 1, 1)

        self.page3ShowErrorsBtn = QPushButton(self.page_3)
        self.page3ShowErrorsBtn.setObjectName(u"page3ShowErrorsBtn")
        self.page3ShowErrorsBtn.setMinimumSize(QSize(152, 0))

        self.gridLayout_4.addWidget(self.page3ShowErrorsBtn, 0, 3, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_3, 0, 1, 1, 1)

        self.page3SetAliasesBtn = QPushButton(self.page_3)
        self.page3SetAliasesBtn.setObjectName(u"page3SetAliasesBtn")
        self.page3SetAliasesBtn.setMinimumSize(QSize(152, 0))

        self.gridLayout_4.addWidget(self.page3SetAliasesBtn, 0, 2, 1, 1)


        self.verticalLayout_4.addLayout(self.gridLayout_4)

        self.stackedWidget.addWidget(self.page_3)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.progressBar = QProgressBar(self.page)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(40, 180, 741, 23))
        self.progressBar.setValue(24)
        self.pushButton = QPushButton(self.page)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(200, 100, 82, 28))
        self.stackedWidget.addWidget(self.page)

        self.verticalLayout.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 943, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.radioOpt1, self.codeEdit)
        QWidget.setTabOrder(self.codeEdit, self.radioOpt2)
        QWidget.setTabOrder(self.radioOpt2, self.rateEdit)
        QWidget.setTabOrder(self.rateEdit, self.page1NextBtn)
        QWidget.setTabOrder(self.page1NextBtn, self.filesList)
        QWidget.setTabOrder(self.filesList, self.destEdit)

        self.retranslateUi(MainWindow)
        self.radioOpt2.toggled.connect(self.destlabel.setEnabled)
        self.radioOpt2.toggled.connect(self.codeLabel.setEnabled)
        self.radioOpt2.toggled.connect(self.rateLabel.setEnabled)
        self.radioOpt2.toggled.connect(self.destEdit.setEnabled)
        self.radioOpt2.toggled.connect(self.codeEdit.setEnabled)
        self.radioOpt2.toggled.connect(self.rateEdit.setEnabled)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Comporator", None))
        self.radioOpt1.setText(QCoreApplication.translate("MainWindow", u"Create LCR from all Supplier Sheets", None))
        self.radioOpt2.setText(QCoreApplication.translate("MainWindow", u"Customize", None))
        self.destlabel.setText(QCoreApplication.translate("MainWindow", u"Enter the Destination:", None))
        self.destEdit.setInputMask("")
        self.codeLabel.setText(QCoreApplication.translate("MainWindow", u"Enter the Dial Code:", None))
        self.codeEdit.setInputMask("")
        self.codeEdit.setText("")
        self.rateLabel.setText(QCoreApplication.translate("MainWindow", u"Enter the Rate:", None))
        self.rateEdit.setInputMask("")
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"Upload customer rate sheet", None))
        self.page1NextBtn.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Add sheets for creating LCR:", None))
        self.p2DellAllBtn.setText(QCoreApplication.translate("MainWindow", u"Delete all", None))
        self.page2NextBtn.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.btnAddFiles.setText(QCoreApplication.translate("MainWindow", u"Add files", None))
        self.btnDelFiles.setText(QCoreApplication.translate("MainWindow", u"Delete selected", None))
        self.page2BackBtn.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        ___qtablewidgetitem = self.clrTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Destination", None));
        ___qtablewidgetitem1 = self.clrTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Codes", None));
        ___qtablewidgetitem2 = self.clrTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Files...", None));
        self.clrErrorLabel.setText(QCoreApplication.translate("MainWindow", u"Errors occurred in the following files:", None))
        self.page3GoBackBtn.setText(QCoreApplication.translate("MainWindow", u"< Back to select option", None))
        self.page3ShowErrorsBtn.setText(QCoreApplication.translate("MainWindow", u"Show sheets errors", None))
        self.page3SetAliasesBtn.setText(QCoreApplication.translate("MainWindow", u"Set aliases", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
    # retranslateUi

