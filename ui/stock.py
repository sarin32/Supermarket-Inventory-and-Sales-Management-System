# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'stock.ui'
##
## Created by: Qt User Interface Compiler version 6.1.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_stock(object):
    def setupUi(self, stock):
        if not stock.objectName():
            stock.setObjectName(u"stock")
        stock.resize(681, 446)
        self.gridLayout = QGridLayout(stock)
        self.gridLayout.setSpacing(2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(stock)
        self.frame_5.setObjectName(u"frame_5")
        self.gridLayout_4 = QGridLayout(self.frame_5)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.tableStock = QTableWidget(self.frame_5)
        if (self.tableStock.columnCount() < 6):
            self.tableStock.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableStock.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableStock.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableStock.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableStock.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableStock.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableStock.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tableStock.setObjectName(u"tableStock")
        self.tableStock.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableStock.sizePolicy().hasHeightForWidth())
        self.tableStock.setSizePolicy(sizePolicy)
        self.tableStock.setMaximumSize(QSize(800, 16777215))
        self.tableStock.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableStock.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableStock.verticalHeader().setVisible(False)

        self.gridLayout_4.addWidget(self.tableStock, 1, 0, 1, 1)

        self.label_5 = QLabel(self.frame_5)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_4.addWidget(self.label_5, 0, 0, 1, 1)

        self.frame_6 = QFrame(self.frame_5)
        self.frame_6.setObjectName(u"frame_6")
        self.horizontalLayout_4 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.buttonUpdateStock = QPushButton(self.frame_6)
        self.buttonUpdateStock.setObjectName(u"buttonUpdateStock")
        self.buttonUpdateStock.setMinimumSize(QSize(125, 0))
        self.buttonUpdateStock.setMaximumSize(QSize(125, 16777215))
        self.buttonUpdateStock.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_4.addWidget(self.buttonUpdateStock)

        self.buttonUpdatePrize = QPushButton(self.frame_6)
        self.buttonUpdatePrize.setObjectName(u"buttonUpdatePrize")
        self.buttonUpdatePrize.setMinimumSize(QSize(125, 0))
        self.buttonUpdatePrize.setMaximumSize(QSize(125, 16777215))
        self.buttonUpdatePrize.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_4.addWidget(self.buttonUpdatePrize)


        self.gridLayout_4.addWidget(self.frame_6, 2, 0, 1, 1, Qt.AlignRight)


        self.gridLayout.addWidget(self.frame_5, 5, 0, 1, 1)

        self.frame_3 = QFrame(stock)
        self.frame_3.setObjectName(u"frame_3")
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame = QFrame(self.frame_3)
        self.frame.setObjectName(u"frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setMaximumSize(QSize(925, 16777215))
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.buttonClear = QPushButton(self.frame_2)
        self.buttonClear.setObjectName(u"buttonClear")
        self.buttonClear.setMinimumSize(QSize(125, 0))
        self.buttonClear.setMaximumSize(QSize(125, 16777215))
        font = QFont()
        font.setFamilies([u"Centular"])
        font.setBold(False)
        font.setItalic(False)
        self.buttonClear.setFont(font)
        self.buttonClear.setCursor(QCursor(Qt.PointingHandCursor))
        self.buttonClear.setIconSize(QSize(16, 16))

        self.horizontalLayout.addWidget(self.buttonClear)

        self.buttonLoad = QPushButton(self.frame_2)
        self.buttonLoad.setObjectName(u"buttonLoad")
        self.buttonLoad.setMinimumSize(QSize(125, 0))
        self.buttonLoad.setMaximumSize(QSize(125, 16777215))
        self.buttonLoad.setFont(font)
        self.buttonLoad.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.buttonLoad)


        self.gridLayout_2.addWidget(self.frame_2, 3, 1, 1, 2, Qt.AlignRight)

        self.fieldCategory = QComboBox(self.frame)
        self.fieldCategory.setObjectName(u"fieldCategory")
        self.fieldCategory.setMinimumSize(QSize(125, 25))
        self.fieldCategory.setMaximumSize(QSize(300, 25))

        self.gridLayout_2.addWidget(self.fieldCategory, 2, 1, 1, 1)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 3)

        self.fieldType = QComboBox(self.frame)
        self.fieldType.addItem("")
        self.fieldType.addItem("")
        self.fieldType.addItem("")
        self.fieldType.setObjectName(u"fieldType")
        self.fieldType.setMinimumSize(QSize(125, 25))
        self.fieldType.setMaximumSize(QSize(300, 25))
        self.fieldType.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.fieldType, 2, 2, 1, 1)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 25))
        self.label_4.setFont(font)

        self.gridLayout_2.addWidget(self.label_4, 1, 1, 1, 1)

        self.fieldBrand = QComboBox(self.frame)
        self.fieldBrand.setObjectName(u"fieldBrand")
        self.fieldBrand.setMinimumSize(QSize(125, 25))
        self.fieldBrand.setMaximumSize(QSize(300, 25))
        self.fieldBrand.setBaseSize(QSize(300, 25))
        self.fieldBrand.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.fieldBrand, 2, 0, 1, 1)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.gridLayout_2.addWidget(self.label_2, 1, 2, 1, 1)


        self.horizontalLayout_2.addWidget(self.frame)

        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")

        self.horizontalLayout_2.addWidget(self.frame_4)


        self.gridLayout.addWidget(self.frame_3, 0, 0, 1, 1)


        self.retranslateUi(stock)

        QMetaObject.connectSlotsByName(stock)
    # setupUi

    def retranslateUi(self, stock):
        stock.setWindowTitle(QCoreApplication.translate("stock", u"Form", None))
        stock.setProperty("type", QCoreApplication.translate("stock", u"main", None))
        self.frame_5.setProperty("type", QCoreApplication.translate("stock", u"mainframe", None))
        ___qtablewidgetitem = self.tableStock.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("stock", u"Product Code", None));
        ___qtablewidgetitem1 = self.tableStock.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("stock", u"Product Name", None));
        ___qtablewidgetitem2 = self.tableStock.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("stock", u"Brand", None));
        ___qtablewidgetitem3 = self.tableStock.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("stock", u"category", None));
        ___qtablewidgetitem4 = self.tableStock.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("stock", u"Stock (Units)", None));
        ___qtablewidgetitem5 = self.tableStock.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("stock", u"Prize/Unit (Rs.)", None));
        self.label_5.setText(QCoreApplication.translate("stock", u"Stock", None))
        self.label_5.setProperty("type", QCoreApplication.translate("stock", u"heading", None))
        self.buttonUpdateStock.setText(QCoreApplication.translate("stock", u"Update Stock", None))
        self.buttonUpdatePrize.setText(QCoreApplication.translate("stock", u"Update Prize", None))
        self.frame_3.setProperty("type", QCoreApplication.translate("stock", u"mainframe", None))
        self.buttonClear.setText(QCoreApplication.translate("stock", u"Clear", None))
        self.buttonLoad.setText(QCoreApplication.translate("stock", u"Load", None))
        self.label.setText(QCoreApplication.translate("stock", u"Filter stock", None))
        self.label.setProperty("type", QCoreApplication.translate("stock", u"heading", None))
        self.fieldType.setItemText(0, QCoreApplication.translate("stock", u"All", None))
        self.fieldType.setItemText(1, QCoreApplication.translate("stock", u"In Stock", None))
        self.fieldType.setItemText(2, QCoreApplication.translate("stock", u"Out Of Stock", None))

        self.label_4.setText(QCoreApplication.translate("stock", u"Catagory", None))
        self.label_3.setText(QCoreApplication.translate("stock", u"Brand", None))
        self.label_2.setText(QCoreApplication.translate("stock", u"Type", None))
    # retranslateUi

