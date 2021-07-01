# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.1.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_login(object):
    def setupUi(self, login):
        if not login.objectName():
            login.setObjectName(u"login")
        login.resize(550, 375)
        login.setMaximumSize(QSize(550, 375))
        self.gridLayout = QGridLayout(login)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 1, 0, 0)
        self.logo = QFrame(login)
        self.logo.setObjectName(u"logo")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logo.sizePolicy().hasHeightForWidth())
        self.logo.setSizePolicy(sizePolicy)
        self.logo.setMinimumSize(QSize(250, 375))
        self.logo.setMaximumSize(QSize(250, 375))
        self.buttonLogo = QPushButton(self.logo)
        self.buttonLogo.setObjectName(u"buttonLogo")
        self.buttonLogo.setGeometry(QRect(90, 30, 80, 80))
        self.buttonLogo.setCursor(QCursor(Qt.PointingHandCursor))
        self.name = QLabel(self.logo)
        self.name.setObjectName(u"name")
        self.name.setGeometry(QRect(10, 260, 231, 61))

        self.gridLayout.addWidget(self.logo, 1, 0, 2, 1)

        self.frameSignIn = QFrame(login)
        self.frameSignIn.setObjectName(u"frameSignIn")
        self.frameSignIn.setMinimumSize(QSize(300, 0))
        self.frameSignIn.setMaximumSize(QSize(300, 16777215))
        self.frameSignIn.setFrameShape(QFrame.StyledPanel)
        self.frameSignIn.setFrameShadow(QFrame.Raised)
        self.fieldUserName = QLineEdit(self.frameSignIn)
        self.fieldUserName.setObjectName(u"fieldUserName")
        self.fieldUserName.setGeometry(QRect(41, 140, 221, 31))
        self.fieldUserName.setMaxLength(10)
        self.labelSignIn = QLabel(self.frameSignIn)
        self.labelSignIn.setObjectName(u"labelSignIn")
        self.labelSignIn.setGeometry(QRect(105, 50, 91, 40))
        self.fieldPwd = QLineEdit(self.frameSignIn)
        self.fieldPwd.setObjectName(u"fieldPwd")
        self.fieldPwd.setGeometry(QRect(40, 230, 221, 31))
        self.fieldPwd.setMaxLength(15)
        self.fieldPwd.setEchoMode(QLineEdit.Password)
        self.buttonSignIn = QPushButton(self.frameSignIn)
        self.buttonSignIn.setObjectName(u"buttonSignIn")
        self.buttonSignIn.setGeometry(QRect(90, 290, 131, 31))
        self.label_2 = QLabel(self.frameSignIn)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 110, 101, 21))
        self.label_3 = QLabel(self.frameSignIn)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(40, 200, 111, 21))

        self.gridLayout.addWidget(self.frameSignIn, 1, 1, 2, 2)


        self.retranslateUi(login)

        QMetaObject.connectSlotsByName(login)
    # setupUi

    def retranslateUi(self, login):
        login.setWindowTitle(QCoreApplication.translate("login", u"Form", None))
        self.buttonLogo.setText("")
        self.name.setText(QCoreApplication.translate("login", u"MASS Supermarket", None))
        self.fieldUserName.setText("")
        self.labelSignIn.setText(QCoreApplication.translate("login", u"Login", None))
        self.fieldPwd.setText("")
        self.buttonSignIn.setText(QCoreApplication.translate("login", u"Login", None))
        self.label_2.setText(QCoreApplication.translate("login", u"User Name", None))
        self.label_3.setText(QCoreApplication.translate("login", u"Password", None))
    # retranslateUi

