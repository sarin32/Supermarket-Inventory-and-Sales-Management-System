# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'products.ui'
##
## Created by: Qt User Interface Compiler version 6.1.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_products(object):
    def setupUi(self, products):
        if not products.objectName():
            products.setObjectName(u"products")
        products.resize(733, 451)
        self.gridLayout = QGridLayout(products)
        self.gridLayout.setSpacing(2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(products)
        self.frame_4.setObjectName(u"frame_4")
        self.gridLayout_5 = QGridLayout(self.frame_4)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.groupBox_2 = QGroupBox(self.frame_4)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_6 = QGridLayout(self.groupBox_2)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")

        self.gridLayout_6.addWidget(self.label, 0, 0, 1, 1)

        self.fieldNewBrand = QLineEdit(self.groupBox_2)
        self.fieldNewBrand.setObjectName(u"fieldNewBrand")
        self.fieldNewBrand.setMinimumSize(QSize(125, 25))
        self.fieldNewBrand.setMaximumSize(QSize(300, 25))

        self.gridLayout_6.addWidget(self.fieldNewBrand, 1, 0, 1, 1)

        self.buttonAddBrand = QPushButton(self.groupBox_2)
        self.buttonAddBrand.setObjectName(u"buttonAddBrand")
        self.buttonAddBrand.setMinimumSize(QSize(125, 0))
        self.buttonAddBrand.setMaximumSize(QSize(125, 16777215))
        self.buttonAddBrand.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_6.addWidget(self.buttonAddBrand, 2, 0, 1, 1, Qt.AlignRight)

        self.gridLayout_5.addWidget(self.groupBox_2, 0, 1, 1, 1, Qt.AlignTop)

        self.tableBrands = QTableWidget(self.frame_4)
        if (self.tableBrands.columnCount() < 2):
            self.tableBrands.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableBrands.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableBrands.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tableBrands.setObjectName(u"tableBrands")
        self.tableBrands.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableBrands.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableBrands.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableBrands.verticalHeader().setVisible(False)

        self.gridLayout_5.addWidget(self.tableBrands, 0, 0, 1, 1, Qt.AlignLeft)

        self.frame_5 = QFrame(self.frame_4)
        self.frame_5.setObjectName(u"frame_5")
        self.horizontalLayout = QHBoxLayout(self.frame_5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.buttonDeleteBrand = QPushButton(self.frame_5)
        self.buttonDeleteBrand.setObjectName(u"buttonDeleteBrand")
        self.buttonDeleteBrand.setMaximumSize(QSize(125, 16777215))
        self.buttonDeleteBrand.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.buttonDeleteBrand)

        self.buttonUpdateBrand = QPushButton(self.frame_5)
        self.buttonUpdateBrand.setObjectName(u"buttonUpdateBrand")
        self.buttonUpdateBrand.setMaximumSize(QSize(125, 16777215))
        self.buttonUpdateBrand.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.buttonUpdateBrand)

        self.gridLayout_5.addWidget(self.frame_5, 1, 0, 1, 1)

        self.gridLayout.addWidget(self.frame_4, 1, 0, 1, 1)

        self.frame_6 = QFrame(products)
        self.frame_6.setObjectName(u"frame_6")
        self.gridLayout_7 = QGridLayout(self.frame_6)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.groupBox_3 = QGroupBox(self.frame_6)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.gridLayout_8 = QGridLayout(self.groupBox_3)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.label_7 = QLabel(self.groupBox_3)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_8.addWidget(self.label_7, 0, 0, 1, 1)

        self.fieldNewCategory = QLineEdit(self.groupBox_3)
        self.fieldNewCategory.setObjectName(u"fieldNewCategory")
        self.fieldNewCategory.setMinimumSize(QSize(125, 25))
        self.fieldNewCategory.setMaximumSize(QSize(300, 25))

        self.gridLayout_8.addWidget(self.fieldNewCategory, 1, 0, 1, 1)

        self.buttonAddCategory = QPushButton(self.groupBox_3)
        self.buttonAddCategory.setObjectName(u"buttonAddCategory")
        self.buttonAddCategory.setMinimumSize(QSize(125, 0))
        self.buttonAddCategory.setMaximumSize(QSize(125, 16777215))
        self.buttonAddCategory.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_8.addWidget(self.buttonAddCategory, 2, 0, 1, 1, Qt.AlignRight)

        self.gridLayout_7.addWidget(self.groupBox_3, 0, 1, 1, 1, Qt.AlignTop)

        self.tableCategories = QTableWidget(self.frame_6)
        if (self.tableCategories.columnCount() < 2):
            self.tableCategories.setColumnCount(2)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableCategories.setHorizontalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableCategories.setHorizontalHeaderItem(1, __qtablewidgetitem3)
        self.tableCategories.setObjectName(u"tableCategories")
        self.tableCategories.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableCategories.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableCategories.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableCategories.verticalHeader().setVisible(False)

        self.gridLayout_7.addWidget(self.tableCategories, 0, 0, 1, 1, Qt.AlignLeft)

        self.frame_7 = QFrame(self.frame_6)
        self.frame_7.setObjectName(u"frame_7")
        self.horizontalLayout_2 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.buttonDeleteCategory = QPushButton(self.frame_7)
        self.buttonDeleteCategory.setObjectName(u"buttonDeleteCategory")
        self.buttonDeleteCategory.setMaximumSize(QSize(125, 16777215))
        self.buttonDeleteCategory.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.buttonDeleteCategory)

        self.buttonUpdateCategory = QPushButton(self.frame_7)
        self.buttonUpdateCategory.setObjectName(u"buttonUpdateCategory")
        self.buttonUpdateCategory.setMaximumSize(QSize(125, 16777215))
        self.buttonUpdateCategory.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_2.addWidget(self.buttonUpdateCategory)

        self.gridLayout_7.addWidget(self.frame_7, 1, 0, 1, 1)

        self.gridLayout.addWidget(self.frame_6, 1, 1, 1, 1)

        self.frame = QFrame(products)
        self.frame.setObjectName(u"frame")
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.horizontalLayout_4 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.buttonDeleteProduct = QPushButton(self.frame_3)
        self.buttonDeleteProduct.setObjectName(u"buttonDeleteProduct")
        self.buttonDeleteProduct.setMinimumSize(QSize(125, 0))
        self.buttonDeleteProduct.setMaximumSize(QSize(125, 16777215))
        self.buttonDeleteProduct.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_4.addWidget(self.buttonDeleteProduct)

        self.buttonUpdateProduct = QPushButton(self.frame_3)
        self.buttonUpdateProduct.setObjectName(u"buttonUpdateProduct")
        self.buttonUpdateProduct.setMinimumSize(QSize(125, 0))
        self.buttonUpdateProduct.setMaximumSize(QSize(125, 16777215))
        self.buttonUpdateProduct.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_4.addWidget(self.buttonUpdateProduct)

        self.gridLayout_2.addWidget(self.frame_3, 3, 0, 1, 1, Qt.AlignRight)

        self.groupBox = QGroupBox(self.frame)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_3 = QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_3.addWidget(self.label_5, 0, 1, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_3.addWidget(self.label_3, 2, 0, 1, 1)

        self.fieldName = QLineEdit(self.groupBox)
        self.fieldName.setObjectName(u"fieldName")
        self.fieldName.setMinimumSize(QSize(125, 25))
        self.fieldName.setMaximumSize(QSize(300, 25))

        self.gridLayout_3.addWidget(self.fieldName, 1, 0, 1, 1)

        self.fieldStock = QSpinBox(self.groupBox)
        self.fieldStock.setObjectName(u"fieldStock")
        self.fieldStock.setMinimumSize(QSize(125, 25))
        self.fieldStock.setMaximumSize(QSize(300, 25))

        self.gridLayout_3.addWidget(self.fieldStock, 1, 1, 1, 1)

        self.fieldCategory = QComboBox(self.groupBox)
        self.fieldCategory.setObjectName(u"fieldCategory")
        self.fieldCategory.setMinimumSize(QSize(125, 25))
        self.fieldCategory.setMaximumSize(QSize(300, 25))

        self.gridLayout_3.addWidget(self.fieldCategory, 5, 0, 1, 1)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_3.addWidget(self.label_4, 4, 0, 1, 1)

        self.fieldBrand = QComboBox(self.groupBox)
        self.fieldBrand.setObjectName(u"fieldBrand")
        self.fieldBrand.setMinimumSize(QSize(125, 25))
        self.fieldBrand.setMaximumSize(QSize(300, 25))

        self.gridLayout_3.addWidget(self.fieldBrand, 3, 0, 1, 1)

        self.fieldPrize = QLineEdit(self.groupBox)
        self.fieldPrize.setObjectName(u"fieldPrize")
        self.fieldPrize.setMinimumSize(QSize(125, 25))
        self.fieldPrize.setMaximumSize(QSize(300, 25))

        self.gridLayout_3.addWidget(self.fieldPrize, 3, 1, 1, 1)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_3.addWidget(self.label_6, 2, 1, 1, 1)

        self.frame_2 = QFrame(self.groupBox)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.buttonAddProduct = QPushButton(self.frame_2)
        self.buttonAddProduct.setObjectName(u"buttonAddProduct")
        self.buttonAddProduct.setMinimumSize(QSize(125, 0))
        self.buttonAddProduct.setMaximumSize(QSize(125, 16777215))
        self.buttonAddProduct.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_4.addWidget(self.buttonAddProduct, 0, 0, 1, 1)

        self.buttonClear = QPushButton(self.frame_2)
        self.buttonClear.setObjectName(u"buttonClear")
        self.buttonClear.setMinimumSize(QSize(125, 0))
        self.buttonClear.setMaximumSize(QSize(125, 16777215))
        self.buttonClear.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_4.addWidget(self.buttonClear, 1, 0, 1, 1)

        self.gridLayout_3.addWidget(self.frame_2, 0, 2, 6, 1)

        self.gridLayout_2.addWidget(self.groupBox, 2, 4, 1, 1)

        self.tableProducts = QTableWidget(self.frame)
        if (self.tableProducts.columnCount() < 2):
            self.tableProducts.setColumnCount(2)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableProducts.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableProducts.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        self.tableProducts.setObjectName(u"tableProducts")
        self.tableProducts.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableProducts.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableProducts.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableProducts.setWordWrap(False)
        self.tableProducts.verticalHeader().setVisible(False)

        self.gridLayout_2.addWidget(self.tableProducts, 2, 0, 1, 1)

        self.gridLayout.addWidget(self.frame, 0, 0, 1, 2)

        self.retranslateUi(products)

        QMetaObject.connectSlotsByName(products)

    # setupUi

    def retranslateUi(self, products):
        products.setWindowTitle(QCoreApplication.translate("products", u"Form", None))
        products.setProperty("type", QCoreApplication.translate("products", u"main", None))
        self.frame_4.setProperty("type", QCoreApplication.translate("products", u"mainframe", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("products", u"Add New Brand", None))
        self.label.setText(QCoreApplication.translate("products", u"Brand Name", None))
        self.buttonAddBrand.setText(QCoreApplication.translate("products", u"Add", None))
        ___qtablewidgetitem = self.tableBrands.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("products", u"Brand Id", None));
        ___qtablewidgetitem1 = self.tableBrands.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("products", u"Brand Name", None));
        self.buttonDeleteBrand.setText(QCoreApplication.translate("products", u"Delete", None))
        self.buttonUpdateBrand.setText(QCoreApplication.translate("products", u"Update", None))
        self.frame_6.setProperty("type", QCoreApplication.translate("products", u"mainframe", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("products", u"Add New Category", None))
        self.label_7.setText(QCoreApplication.translate("products", u"Category Name", None))
        self.buttonAddCategory.setText(QCoreApplication.translate("products", u"Add", None))
        ___qtablewidgetitem2 = self.tableCategories.horizontalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("products", u"Category Id", None));
        ___qtablewidgetitem3 = self.tableCategories.horizontalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("products", u"Category Name", None));
        self.buttonDeleteCategory.setText(QCoreApplication.translate("products", u"Delete", None))
        self.buttonUpdateCategory.setText(QCoreApplication.translate("products", u"Update", None))
        self.frame.setProperty("type", QCoreApplication.translate("products", u"mainframe", None))
        self.buttonDeleteProduct.setText(QCoreApplication.translate("products", u"Delete", None))
        self.buttonUpdateProduct.setText(QCoreApplication.translate("products", u"Update", None))
        self.groupBox.setTitle(QCoreApplication.translate("products", u"Add New Product", None))
        self.label_5.setText(QCoreApplication.translate("products", u"Current Stock", None))
        self.label_2.setText(QCoreApplication.translate("products", u"Product Name", None))
        self.label_3.setText(QCoreApplication.translate("products", u"Brand", None))
        self.label_4.setText(QCoreApplication.translate("products", u"Category", None))
        self.label_6.setText(QCoreApplication.translate("products", u"Prize/Unit", None))
        self.buttonAddProduct.setText(QCoreApplication.translate("products", u"Add", None))
        self.buttonClear.setText(QCoreApplication.translate("products", u"Clear", None))
        ___qtablewidgetitem4 = self.tableProducts.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("products", u"Product Id", None));
        ___qtablewidgetitem5 = self.tableProducts.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("products", u"Product Name", None));
    # retranslateUi
