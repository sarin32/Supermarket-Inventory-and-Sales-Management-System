# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'addUser.ui'
##
## Created by: Qt User Interface Compiler version 6.1.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_addUser(object):
    def setupUi(self, addUser):
        if not addUser.objectName():
            addUser.setObjectName(u"addUser")
        addUser.resize(280, 301)
        self.label = QLabel(addUser)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 261, 31))
        self.label_2 = QLabel(addUser)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 90, 261, 31))
        self.fieldUsername = QLineEdit(addUser)
        self.fieldUsername.setObjectName(u"fieldUsername")
        self.fieldUsername.setGeometry(QRect(10, 50, 261, 31))
        self.fieldPwd = QLineEdit(addUser)
        self.fieldPwd.setObjectName(u"fieldPwd")
        self.fieldPwd.setGeometry(QRect(12, 130, 261, 31))
        self.fieldPwd.setEchoMode(QLineEdit.Password)
        self.label_3 = QLabel(addUser)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 170, 261, 31))
        self.fieldCnfrmPwd = QLineEdit(addUser)
        self.fieldCnfrmPwd.setObjectName(u"fieldCnfrmPwd")
        self.fieldCnfrmPwd.setGeometry(QRect(10, 210, 261, 31))
        self.fieldCnfrmPwd.setEchoMode(QLineEdit.Password)
        self.buttonAddUser = QPushButton(addUser)
        self.buttonAddUser.setObjectName(u"buttonAddUser")
        self.buttonAddUser.setGeometry(QRect(150, 260, 121, 31))
        self.buttonCancel = QPushButton(addUser)
        self.buttonCancel.setObjectName(u"buttonCancel")
        self.buttonCancel.setGeometry(QRect(10, 260, 121, 31))

        self.retranslateUi(addUser)

        QMetaObject.connectSlotsByName(addUser)
    # setupUi

    def retranslateUi(self, addUser):
        addUser.setWindowTitle(QCoreApplication.translate("addUser", u"Form", None))
        self.label.setText(QCoreApplication.translate("addUser", u"User Name", None))
        self.label_2.setText(QCoreApplication.translate("addUser", u"Password", None))
        self.label_3.setText(QCoreApplication.translate("addUser", u"Confirm Password", None))
        self.buttonAddUser.setText(QCoreApplication.translate("addUser", u"Add User", None))
        self.buttonCancel.setText(QCoreApplication.translate("addUser", u"Cancel", None))
    # retranslateUi

