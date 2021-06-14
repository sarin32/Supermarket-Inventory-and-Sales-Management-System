# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sales.ui'
##
## Created by: Qt User Interface Compiler version 6.1.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_sales(object):
    def setupUi(self, sales):
        if not sales.objectName():
            sales.setObjectName(u"sales")
        sales.resize(847, 565)
        sales.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(sales)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.mainframe_1 = QFrame(sales)
        self.mainframe_1.setObjectName(u"mainframe_1")
        self.mainframe_1.setStyleSheet(u"")
        self.mainframe_1.setFrameShape(QFrame.StyledPanel)
        self.mainframe_1.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.mainframe_1)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_2 = QFrame(self.mainframe_1)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 60))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.tableSales = QTableWidget(self.frame_2)
        if (self.tableSales.columnCount() < 4):
            self.tableSales.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableSales.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableSales.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableSales.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableSales.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableSales.setObjectName(u"tableSales")
        self.tableSales.setMaximumSize(QSize(500, 16777215))
        self.tableSales.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableSales.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableSales.verticalHeader().setVisible(False)

        self.gridLayout_2.addWidget(self.tableSales, 1, 0, 1, 1)

        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 30))
        self.frame_5.setMaximumSize(QSize(16777215, 30))
        self.horizontalLayout_2 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.labelTotal = QLabel(self.frame_5)
        self.labelTotal.setObjectName(u"labelTotal")

        self.horizontalLayout_2.addWidget(self.labelTotal)

        self.labeldailyAmount = QLabel(self.frame_5)
        self.labeldailyAmount.setObjectName(u"labeldailyAmount")

        self.horizontalLayout_2.addWidget(self.labeldailyAmount)

        self.labelRs = QLabel(self.frame_5)
        self.labelRs.setObjectName(u"labelRs")

        self.horizontalLayout_2.addWidget(self.labelRs)


        self.horizontalLayout.addWidget(self.frame_5, 0, Qt.AlignLeft)


        self.gridLayout_2.addWidget(self.frame_3, 2, 0, 1, 1)


        self.gridLayout.addWidget(self.frame_2, 2, 0, 2, 2)

        self.frame = QFrame(self.mainframe_1)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(340, 280))
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_2.addWidget(self.label_5)

        self.calendar = QCalendarWidget(self.frame)
        self.calendar.setObjectName(u"calendar")

        self.verticalLayout_2.addWidget(self.calendar)

        self.buttonLoad = QPushButton(self.frame)
        self.buttonLoad.setObjectName(u"buttonLoad")
        self.buttonLoad.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_2.addWidget(self.buttonLoad, 0, Qt.AlignRight)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.groupBox_2 = QGroupBox(self.mainframe_1)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMaximumSize(QSize(16777215, 300))
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_4.addWidget(self.label_3)

        self.fieldMonth = QComboBox(self.groupBox_2)
        self.fieldMonth.addItem("")
        self.fieldMonth.addItem("")
        self.fieldMonth.addItem("")
        self.fieldMonth.addItem("")
        self.fieldMonth.addItem("")
        self.fieldMonth.addItem("")
        self.fieldMonth.addItem("")
        self.fieldMonth.addItem("")
        self.fieldMonth.addItem("")
        self.fieldMonth.addItem("")
        self.fieldMonth.addItem("")
        self.fieldMonth.addItem("")
        self.fieldMonth.setObjectName(u"fieldMonth")
        self.fieldMonth.setMinimumSize(QSize(125, 25))
        self.fieldMonth.setMaximumSize(QSize(300, 25))

        self.verticalLayout_4.addWidget(self.fieldMonth)

        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")
        font = QFont()
        font.setFamilies([u"Centular"])
        font.setBold(False)
        font.setItalic(False)
        self.label_4.setFont(font)

        self.verticalLayout_4.addWidget(self.label_4)

        self.fieldYear = QComboBox(self.groupBox_2)
        self.fieldYear.setObjectName(u"fieldYear")
        self.fieldYear.setMinimumSize(QSize(125, 25))
        self.fieldYear.setMaximumSize(QSize(300, 25))

        self.verticalLayout_4.addWidget(self.fieldYear)

        self.frame_6 = QFrame(self.groupBox_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(0, 30))
        self.frame_6.setMaximumSize(QSize(16777215, 30))
        self.horizontalLayout_3 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.labelTotal_2 = QLabel(self.frame_6)
        self.labelTotal_2.setObjectName(u"labelTotal_2")

        self.horizontalLayout_3.addWidget(self.labelTotal_2)

        self.labelMonthlyAmount = QLabel(self.frame_6)
        self.labelMonthlyAmount.setObjectName(u"labelMonthlyAmount")

        self.horizontalLayout_3.addWidget(self.labelMonthlyAmount)

        self.labelRs_2 = QLabel(self.frame_6)
        self.labelRs_2.setObjectName(u"labelRs_2")

        self.horizontalLayout_3.addWidget(self.labelRs_2)


        self.verticalLayout_4.addWidget(self.frame_6, 0, Qt.AlignLeft)

        self.buttonCheck = QPushButton(self.groupBox_2)
        self.buttonCheck.setObjectName(u"buttonCheck")
        self.buttonCheck.setMaximumSize(QSize(100, 25))
        self.buttonCheck.setFont(font)
        self.buttonCheck.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.buttonCheck)


        self.gridLayout.addWidget(self.groupBox_2, 0, 1, 1, 1)


        self.verticalLayout.addWidget(self.mainframe_1)


        self.retranslateUi(sales)

        QMetaObject.connectSlotsByName(sales)
    # setupUi

    def retranslateUi(self, sales):
        sales.setWindowTitle(QCoreApplication.translate("sales", u"Form", None))
        sales.setProperty("type", QCoreApplication.translate("sales", u"main", None))
        self.mainframe_1.setProperty("type", QCoreApplication.translate("sales", u"mainframe", None))
        self.label.setText(QCoreApplication.translate("sales", u"Sales", None))
        self.label.setProperty("type", QCoreApplication.translate("sales", u"heading", None))
        ___qtablewidgetitem = self.tableSales.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("sales", u"Sale Id", None));
        ___qtablewidgetitem1 = self.tableSales.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("sales", u"Date", None));
        ___qtablewidgetitem2 = self.tableSales.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("sales", u"Time", None));
        ___qtablewidgetitem3 = self.tableSales.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("sales", u"Amount", None));
        self.labelTotal.setText(QCoreApplication.translate("sales", u"Total Amount :", None))
        self.labeldailyAmount.setText(QCoreApplication.translate("sales", u"0.0", None))
        self.labeldailyAmount.setProperty("type", QCoreApplication.translate("sales", u"bold", None))
        self.labelRs.setText(QCoreApplication.translate("sales", u"Rs.", None))
        self.label_5.setText(QCoreApplication.translate("sales", u"View Sales", None))
        self.label_5.setProperty("type", QCoreApplication.translate("sales", u"heading", None))
        self.buttonLoad.setText(QCoreApplication.translate("sales", u"Load", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("sales", u"Monthly sale", None))
        self.label_3.setText(QCoreApplication.translate("sales", u"Month", None))
        self.fieldMonth.setItemText(0, QCoreApplication.translate("sales", u"January", None))
        self.fieldMonth.setItemText(1, QCoreApplication.translate("sales", u"February", None))
        self.fieldMonth.setItemText(2, QCoreApplication.translate("sales", u"March", None))
        self.fieldMonth.setItemText(3, QCoreApplication.translate("sales", u"April", None))
        self.fieldMonth.setItemText(4, QCoreApplication.translate("sales", u"May", None))
        self.fieldMonth.setItemText(5, QCoreApplication.translate("sales", u"June", None))
        self.fieldMonth.setItemText(6, QCoreApplication.translate("sales", u"July", None))
        self.fieldMonth.setItemText(7, QCoreApplication.translate("sales", u"August", None))
        self.fieldMonth.setItemText(8, QCoreApplication.translate("sales", u"September", None))
        self.fieldMonth.setItemText(9, QCoreApplication.translate("sales", u"October", None))
        self.fieldMonth.setItemText(10, QCoreApplication.translate("sales", u"November", None))
        self.fieldMonth.setItemText(11, QCoreApplication.translate("sales", u"December", None))

        self.label_4.setText(QCoreApplication.translate("sales", u"Year", None))
        self.labelTotal_2.setText(QCoreApplication.translate("sales", u"Sale Amount", None))
        self.labelMonthlyAmount.setText(QCoreApplication.translate("sales", u"0.0", None))
        self.labelMonthlyAmount.setProperty("type", QCoreApplication.translate("sales", u"bold", None))
        self.labelRs_2.setText(QCoreApplication.translate("sales", u"Rs.", None))
        self.buttonCheck.setText(QCoreApplication.translate("sales", u"Check", None))
    # retranslateUi

