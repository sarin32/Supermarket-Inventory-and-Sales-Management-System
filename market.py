from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class Cart:
    def __init__(self):
        self.cart = []
        self.total_cost = 0

    def newProduct(self, product_code, units):
        pass

    def purchase(self):
        pass


class Inventory:
    def __init__(self):
        self.brandIds = ['25', '36']
        self.categoryIds = ['36', '45']
        self.productIds = ['65', '36']

    def getAllBrandNames(self):
        return self.brandIds

    def getAllCategoryNames(self):
        return self.categoryIds

    def getAllProductNames(self, brandId=None, categoryId=None):
        return self.productIds


class Ui_MainWindow(object):
    def __init__(self):
        self.crt = Cart()
        self.inv = Inventory()
        self.setupUi(MainWindow)

        # initialize combobox
        self.fieldBrand.addItem('select')
        self.fieldBrand.addItems(self.inv.getAllBrandNames())
        self.fieldCategory.addItem('select')
        self.fieldCategory.addItems(self.inv.getAllCategoryNames())
        self.fieldName.addItem('select')
        self.fieldName.addItems(self.inv.getAllProductNames())

        # event updates
        self.buttonClear.clicked.connect(self.clear)
        self.buttonAdd.clicked.connect(self.AddToCart)
        self.fieldCategory.currentIndexChanged.connect(self.updateProductNames)
        self.fieldBrand.currentIndexChanged.connect(self.updateProductNames)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(793, 542)
        MainWindow.setStyleSheet("QLabel{\n"
                                 "    font: 75 bold 10pt  \"MS Sans Serif\";\n"
                                 "}\n"
                                 "\n"
                                 "QLabel#labelCart , QLabel#labelSearchProduct{\n"
                                 "    font: 75 bold 15pt  \"MS Sans Serif\";\n"
                                 "}\n"
                                 "\n"
                                 "QFrame#frameSearchProduct, QFrame#frameCart{\n"
                                 "    background-color:rgb(202, 202, 202);\n"
                                 "    border-radius:6px;\n"
                                 "}\n"
                                 "\n"
                                 "QComboBox,QSpinBox{\n"
                                 "    background-color:#eee;\n"
                                 "    border: 0.1em solid;\n"
                                 "    color:#000;\n"
                                 "    border-radius:5px;\n"
                                 "}\n"
                                 "")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frameCart = QtWidgets.QFrame(self.centralwidget)
        self.frameCart.setEnabled(True)
        self.frameCart.setStyleSheet("")
        self.frameCart.setObjectName("frameCart")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frameCart)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.frameCost = QtWidgets.QFrame(self.frameCart)
        self.frameCost.setMinimumSize(QtCore.QSize(0, 30))
        self.frameCost.setMaximumSize(QtCore.QSize(16777215, 30))
        self.frameCost.setObjectName("frameCost")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frameCost)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.labelTotal = QtWidgets.QLabel(self.frameCost)
        self.labelTotal.setStyleSheet("")
        self.labelTotal.setObjectName("labelTotal")
        self.horizontalLayout_2.addWidget(self.labelTotal)
        self.labelCost = QtWidgets.QLabel(self.frameCost)
        self.labelCost.setStyleSheet("")
        self.labelCost.setObjectName("labelCost")
        self.horizontalLayout_2.addWidget(self.labelCost)
        self.labelRs = QtWidgets.QLabel(self.frameCost)
        self.labelRs.setStyleSheet("")
        self.labelRs.setObjectName("labelRs")
        self.horizontalLayout_2.addWidget(self.labelRs)
        self.gridLayout_4.addWidget(self.frameCost, 3, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.frameCartButtons = QtWidgets.QFrame(self.frameCart)
        self.frameCartButtons.setMinimumSize(QtCore.QSize(0, 50))
        self.frameCartButtons.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frameCartButtons.setObjectName("frameCartButtons")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frameCartButtons)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.buttonClearAll = QtWidgets.QPushButton(self.frameCartButtons)
        self.buttonClearAll.setMinimumSize(QtCore.QSize(125, 0))
        self.buttonClearAll.setMaximumSize(QtCore.QSize(125, 16777215))
        self.buttonClearAll.setObjectName("buttonClearAll")
        self.horizontalLayout_3.addWidget(self.buttonClearAll)
        self.buttonRemove = QtWidgets.QPushButton(self.frameCartButtons)
        self.buttonRemove.setMinimumSize(QtCore.QSize(125, 0))
        self.buttonRemove.setMaximumSize(QtCore.QSize(125, 16777215))
        self.buttonRemove.setObjectName("buttonRemove")
        self.horizontalLayout_3.addWidget(self.buttonRemove)
        self.buttonPurchase = QtWidgets.QPushButton(self.frameCartButtons)
        self.buttonPurchase.setMinimumSize(QtCore.QSize(125, 0))
        self.buttonPurchase.setMaximumSize(QtCore.QSize(125, 16777215))
        self.buttonPurchase.setObjectName("buttonPurchase")
        self.horizontalLayout_3.addWidget(self.buttonPurchase)
        self.gridLayout_4.addWidget(self.frameCartButtons, 3, 1, 1, 1, QtCore.Qt.AlignRight)
        self.tableCart = QtWidgets.QTableWidget(self.frameCart)
        self.tableCart.setEnabled(True)
        self.tableCart.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.tableCart.setGridStyle(QtCore.Qt.DashLine)
        self.tableCart.setObjectName("tableCart")
        self.tableCart.setColumnCount(7)
        self.tableCart.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableCart.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableCart.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableCart.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableCart.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableCart.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableCart.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableCart.setHorizontalHeaderItem(6, item)
        self.gridLayout_4.addWidget(self.tableCart, 2, 0, 1, 2, QtCore.Qt.AlignHCenter)
        self.labelCart = QtWidgets.QLabel(self.frameCart)
        self.labelCart.setMinimumSize(QtCore.QSize(0, 30))
        self.labelCart.setMaximumSize(QtCore.QSize(16777215, 30))
        self.labelCart.setStyleSheet("")
        self.labelCart.setObjectName("labelCart")
        self.gridLayout_4.addWidget(self.labelCart, 0, 0, 1, 2)
        self.gridLayout.addWidget(self.frameCart, 1, 0, 1, 1)
        self.frameSearchProduct = QtWidgets.QFrame(self.centralwidget)
        self.frameSearchProduct.setMinimumSize(QtCore.QSize(0, 170))
        self.frameSearchProduct.setMaximumSize(QtCore.QSize(16777215, 170))
        self.frameSearchProduct.setStyleSheet("")
        self.frameSearchProduct.setObjectName("frameSearchProduct")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frameSearchProduct)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.fieldUnits = QtWidgets.QSpinBox(self.frameSearchProduct)
        self.fieldUnits.setMinimumSize(QtCore.QSize(125, 25))
        self.fieldUnits.setStyleSheet("")
        self.fieldUnits.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.fieldUnits.setObjectName("fieldUnits")
        self.gridLayout_2.addWidget(self.fieldUnits, 17, 4, 1, 1)
        self.labelCategory = QtWidgets.QLabel(self.frameSearchProduct)
        self.labelCategory.setStyleSheet("")
        self.labelCategory.setObjectName("labelCategory")
        self.gridLayout_2.addWidget(self.labelCategory, 6, 2, 1, 1)
        self.fieldCode = QtWidgets.QSpinBox(self.frameSearchProduct)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fieldCode.sizePolicy().hasHeightForWidth())
        self.fieldCode.setSizePolicy(sizePolicy)
        self.fieldCode.setMinimumSize(QtCore.QSize(125, 25))
        self.fieldCode.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.fieldCode.setStyleSheet("")
        self.fieldCode.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.fieldCode.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToPreviousValue)
        self.fieldCode.setStepType(QtWidgets.QAbstractSpinBox.DefaultStepType)
        self.fieldCode.setObjectName("fieldCode")
        self.gridLayout_2.addWidget(self.fieldCode, 17, 0, 1, 1)
        self.fieldName = QtWidgets.QComboBox(self.frameSearchProduct)
        self.fieldName.setMinimumSize(QtCore.QSize(125, 25))
        self.fieldName.setStyleSheet("")
        self.fieldName.setObjectName("fieldName")
        self.gridLayout_2.addWidget(self.fieldName, 17, 1, 1, 1)
        self.labelUnits = QtWidgets.QLabel(self.frameSearchProduct)
        self.labelUnits.setStyleSheet("")
        self.labelUnits.setObjectName("labelUnits")
        self.gridLayout_2.addWidget(self.labelUnits, 6, 4, 1, 1)
        self.fieldCategory = QtWidgets.QComboBox(self.frameSearchProduct)
        self.fieldCategory.setMinimumSize(QtCore.QSize(125, 25))
        self.fieldCategory.setStyleSheet("")
        self.fieldCategory.setObjectName("fieldCategory")
        self.gridLayout_2.addWidget(self.fieldCategory, 17, 2, 1, 1)
        self.frameSearchButtons = QtWidgets.QFrame(self.frameSearchProduct)
        self.frameSearchButtons.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frameSearchButtons.setStyleSheet("")
        self.frameSearchButtons.setObjectName("frameSearchButtons")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frameSearchButtons)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.buttonClear = QtWidgets.QPushButton(self.frameSearchButtons)
        self.buttonClear.setMinimumSize(QtCore.QSize(125, 0))
        self.buttonClear.setMaximumSize(QtCore.QSize(125, 16777215))
        self.buttonClear.setIconSize(QtCore.QSize(16, 16))
        self.buttonClear.setObjectName("buttonClear")
        self.horizontalLayout.addWidget(self.buttonClear)
        self.buttonAdd = QtWidgets.QPushButton(self.frameSearchButtons)
        self.buttonAdd.setMinimumSize(QtCore.QSize(125, 0))
        self.buttonAdd.setMaximumSize(QtCore.QSize(125, 16777215))
        self.buttonAdd.setObjectName("buttonAdd")
        self.horizontalLayout.addWidget(self.buttonAdd)
        self.gridLayout_2.addWidget(self.frameSearchButtons, 18, 3, 1, 2, QtCore.Qt.AlignRight)
        self.labelBrand = QtWidgets.QLabel(self.frameSearchProduct)
        self.labelBrand.setStyleSheet("")
        self.labelBrand.setObjectName("labelBrand")
        self.gridLayout_2.addWidget(self.labelBrand, 6, 3, 1, 1)
        self.labelSearchProduct = QtWidgets.QLabel(self.frameSearchProduct)
        self.labelSearchProduct.setEnabled(True)
        self.labelSearchProduct.setMinimumSize(QtCore.QSize(0, 30))
        self.labelSearchProduct.setMaximumSize(QtCore.QSize(16777215, 30))
        self.labelSearchProduct.setStyleSheet("")
        self.labelSearchProduct.setObjectName("labelSearchProduct")
        self.gridLayout_2.addWidget(self.labelSearchProduct, 0, 0, 1, 4)
        self.fieldBrand = QtWidgets.QComboBox(self.frameSearchProduct)
        self.fieldBrand.setMinimumSize(QtCore.QSize(125, 25))
        self.fieldBrand.setStyleSheet("")
        self.fieldBrand.setObjectName("fieldBrand")
        self.gridLayout_2.addWidget(self.fieldBrand, 17, 3, 1, 1)
        self.labelCode = QtWidgets.QLabel(self.frameSearchProduct)
        self.labelCode.setStyleSheet("")
        self.labelCode.setObjectName("labelCode")
        self.gridLayout_2.addWidget(self.labelCode, 6, 0, 1, 1)
        self.labelName = QtWidgets.QLabel(self.frameSearchProduct)
        self.labelName.setMaximumSize(QtCore.QSize(16777215, 25))
        self.labelName.setStyleSheet("")
        self.labelName.setObjectName("labelName")
        self.gridLayout_2.addWidget(self.labelName, 6, 1, 1, 1)
        self.gridLayout.addWidget(self.frameSearchProduct, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 793, 21))
        self.menubar.setObjectName("menubar")
        self.menuPurchase = QtWidgets.QMenu(self.menubar)
        self.menuPurchase.setObjectName("menuPurchase")
        self.menuAddCommodity = QtWidgets.QMenu(self.menubar)
        self.menuAddCommodity.setObjectName("menuAddCommodity")
        self.menuRemoveCommodity = QtWidgets.QMenu(self.menubar)
        self.menuRemoveCommodity.setObjectName("menuRemoveCommodity")
        self.menuUpdateCommodity = QtWidgets.QMenu(self.menubar)
        self.menuUpdateCommodity.setObjectName("menuUpdateCommodity")
        self.menuStockEnquiry = QtWidgets.QMenu(self.menubar)
        self.menuStockEnquiry.setObjectName("menuStockEnquiry")
        MainWindow.setMenuBar(self.menubar)
        self.menubar.addAction(self.menuPurchase.menuAction())
        self.menubar.addAction(self.menuAddCommodity.menuAction())
        self.menubar.addAction(self.menuRemoveCommodity.menuAction())
        self.menubar.addAction(self.menuUpdateCommodity.menuAction())
        self.menubar.addAction(self.menuStockEnquiry.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MASS Supermarket"))
        MainWindow.setWindowIcon(QtGui.QIcon('res/images/icon.png'))
        self.labelTotal.setText(_translate("MainWindow", "Total Cost :"))
        self.labelCost.setText(_translate("MainWindow", "0.0"))
        self.labelRs.setText(_translate("MainWindow", "Rs."))
        self.buttonClearAll.setText(_translate("MainWindow", "Clear All"))
        self.buttonRemove.setText(_translate("MainWindow", "Remove"))
        self.buttonPurchase.setText(_translate("MainWindow", "Purchase"))
        self.tableCart.setSortingEnabled(False)
        item = self.tableCart.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Product Code"))
        item = self.tableCart.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Product Name"))
        item = self.tableCart.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Brand"))
        item = self.tableCart.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "category"))
        item = self.tableCart.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Units"))
        item = self.tableCart.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Cost/Unit"))
        item = self.tableCart.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Cost"))
        self.labelCart.setText(_translate("MainWindow", "Cart"))
        self.labelCategory.setText(_translate("MainWindow", "Category"))
        self.labelUnits.setText(_translate("MainWindow", "Units"))
        self.buttonClear.setText(_translate("MainWindow", "Clear"))
        self.buttonAdd.setText(_translate("MainWindow", "Add to cart"))
        self.labelBrand.setText(_translate("MainWindow", "Brand"))
        self.labelSearchProduct.setText(_translate("MainWindow", "Search Product"))
        self.labelCode.setText(_translate("MainWindow", "Product Code"))
        self.labelName.setText(_translate("MainWindow", "Product Name"))
        self.menuPurchase.setTitle(_translate("MainWindow", "Purchase"))
        self.menuAddCommodity.setTitle(_translate("MainWindow", "Add Commodity"))
        self.menuRemoveCommodity.setTitle(_translate("MainWindow", "Remove Commodity"))
        self.menuUpdateCommodity.setTitle(_translate("MainWindow", "Update Commodity"))
        self.menuStockEnquiry.setTitle(_translate("MainWindow", "Stock Enquiry"))

    def clear(self):
        self.fieldCode.setValue(0)
        self.fieldUnits.setValue(0)
        self.fieldName.clear()
        self.fieldName.addItem('select')
        self.fieldName.addItems(self.inv.getAllProductNames())
        self.fieldCategory.setCurrentIndex(0)
        self.fieldBrand.setCurrentIndex(0)

    def AddToCart(self):
        # TODO: validate fields
        self.crt.newProduct(self.fieldCode, self.fieldUnits)

    def updateProductNames(self):
        if self.fieldBrand.currentText() == 'select' and self.fieldCategory.currentText() == 'select':
            self.inv.getAllProductNames()
        elif self.fieldBrand.currentText() == 'select':
            self.inv.getAllProductNames(brandId=None, categoryId=self.fieldCategory.currentText())
        elif self.fieldCategory.currentText() == 'select':
            self.inv.getAllProductNames(brandId=self.fieldBrand)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    MainWindow.show()
    sys.exit(app.exec_())
