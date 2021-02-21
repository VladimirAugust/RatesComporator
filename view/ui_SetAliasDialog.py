# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SetAliasDialog.ui'
##
## Created by: Qt User Interface Compiler version 6.0.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_SetAliasDialog(object):
    def setupUi(self, SetAliasDialog):
        if not SetAliasDialog.objectName():
            SetAliasDialog.setObjectName(u"SetAliasDialog")
        SetAliasDialog.setWindowModality(Qt.ApplicationModal)
        SetAliasDialog.setEnabled(True)
        SetAliasDialog.resize(557, 196)
        SetAliasDialog.setCursor(QCursor(Qt.ArrowCursor))
        SetAliasDialog.setMouseTracking(False)
        self.verticalLayout = QVBoxLayout(SetAliasDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(SetAliasDialog)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(15)
        self.destLabel = QLabel(SetAliasDialog)
        self.destLabel.setObjectName(u"destLabel")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.destLabel)

        self.destAlias = QLineEdit(SetAliasDialog)
        self.destAlias.setObjectName(u"destAlias")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.destAlias)

        self.codeLabel = QLabel(SetAliasDialog)
        self.codeLabel.setObjectName(u"codeLabel")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.codeLabel)

        self.codeAlias = QLineEdit(SetAliasDialog)
        self.codeAlias.setObjectName(u"codeAlias")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.codeAlias)

        self.rateLabel = QLabel(SetAliasDialog)
        self.rateLabel.setObjectName(u"rateLabel")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.rateLabel)

        self.rateAlias = QLineEdit(SetAliasDialog)
        self.rateAlias.setObjectName(u"rateAlias")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.rateAlias)


        self.verticalLayout.addLayout(self.formLayout)

        self.errorLabel = QLabel(SetAliasDialog)
        self.errorLabel.setObjectName(u"errorLabel")
        self.errorLabel.setMaximumSize(QSize(16777215, 20))
        self.errorLabel.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.errorLabel, 0, Qt.AlignHCenter)

        self.buttonBox = QDialogButtonBox(SetAliasDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setMinimumSize(QSize(442, 0))
        self.buttonBox.setMaximumSize(QSize(442, 16777215))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(SetAliasDialog)
        self.buttonBox.accepted.connect(SetAliasDialog.accept)
        self.buttonBox.rejected.connect(SetAliasDialog.reject)

        QMetaObject.connectSlotsByName(SetAliasDialog)
    # setupUi

    def retranslateUi(self, SetAliasDialog):
        SetAliasDialog.setWindowTitle(QCoreApplication.translate("SetAliasDialog", u"Set Alias", None))
        self.label.setText(QCoreApplication.translate("SetAliasDialog", u"You can list aliases separated by commas (eg: \"destination, country\")", None))
        self.destLabel.setText(QCoreApplication.translate("SetAliasDialog", u"Destination alias:", None))
#if QT_CONFIG(tooltip)
        self.destAlias.setToolTip("")
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.destAlias.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.codeLabel.setText(QCoreApplication.translate("SetAliasDialog", u"Code alias:", None))
        self.rateLabel.setText(QCoreApplication.translate("SetAliasDialog", u"Rate alias:", None))
        self.errorLabel.setText("")
    # retranslateUi

