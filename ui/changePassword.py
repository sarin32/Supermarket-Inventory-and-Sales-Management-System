# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'changePassword.ui'
##
## Created by: Qt User Interface Compiler version 6.1.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_changePassword(object):
    def setupUi(self, changePassword):
        if not changePassword.objectName():
            changePassword.setObjectName(u"changePassword")
        changePassword.resize(280, 221)
        self.label = QLabel(changePassword)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 261, 31))
        self.label_2 = QLabel(changePassword)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 90, 261, 31))
        self.fieldPwd = QLineEdit(changePassword)
        self.fieldPwd.setObjectName(u"fieldPwd")
        self.fieldPwd.setGeometry(QRect(10, 50, 261, 31))
        self.fieldPwd.setEchoMode(QLineEdit.Password)
        self.fieldCnfrmPwd = QLineEdit(changePassword)
        self.fieldCnfrmPwd.setObjectName(u"fieldCnfrmPwd")
        self.fieldCnfrmPwd.setGeometry(QRect(12, 130, 261, 31))
        self.fieldCnfrmPwd.setEchoMode(QLineEdit.Password)
        self.buttonChangePassword = QPushButton(changePassword)
        self.buttonChangePassword.setObjectName(u"buttonChangePassword")
        self.buttonChangePassword.setGeometry(QRect(150, 180, 121, 31))
        self.buttonCancel = QPushButton(changePassword)
        self.buttonCancel.setObjectName(u"buttonCancel")
        self.buttonCancel.setGeometry(QRect(10, 180, 121, 31))

        self.retranslateUi(changePassword)

        QMetaObject.connectSlotsByName(changePassword)
    # setupUi

    def retranslateUi(self, changePassword):
        changePassword.setWindowTitle(QCoreApplication.translate("changePassword", u"Form", None))
        self.label.setText(QCoreApplication.translate("changePassword", u"New Password", None))
        self.label_2.setText(QCoreApplication.translate("changePassword", u"Confirm Password", None))
        self.buttonChangePassword.setText(QCoreApplication.translate("changePassword", u"Change Password", None))
        self.buttonCancel.setText(QCoreApplication.translate("changePassword", u"Cancel", None))
    # retranslateUi

