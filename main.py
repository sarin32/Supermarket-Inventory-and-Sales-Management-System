"""
This is the runner file of the application
Mainwindow is created and other widgets are added in this file
"""
import sys

from PyQt5.QtCore import QRect
from PyQt5.QtGui import QIcon, QDoubleValidator
from PyQt5.QtWidgets import QApplication, QMenuBar, QMainWindow, QStackedWidget, QWidget, QMessageBox

from superMarket import Cart, Inventory
from ui.products import Ui_products
from ui.purchase import Ui_purchase


class UIProducts(Ui_products):
    def __init__(self, widget,crt,inv):
        self.widget = widget
        self.crt = crt
        self.inv = inv
        self.setupUi(widget)
        self.fieldPrize.setValidator(QDoubleValidator(0, 10000, 2))
        # initialize combobox
        self.fieldBrand.addItem('select')
        self.fieldBrand.addItems(self.inv.getAllBrandNames())
        self.fieldCategory.addItem('select')
        self.fieldCategory.addItems(self.inv.getAllCategoryNames())
        # event updates
        self.buttonClear.clicked.connect(lambda: self.clear())
        self.buttonAddProduct.clicked.connect(lambda: self.addProduct())
        self.buttonAddBrand.clicked.connect(lambda: self.addBrand())
        self.buttonAddCategory.clicked.connect(lambda: self.addCategory())

    def clear(self):
        self.fieldPrize.clear()
        self.fieldStock.setValue(0)
        self.fieldName.clear()
        self.fieldCategory.setCurrentIndex(0)
        self.fieldBrand.setCurrentIndex(0)

    def addProduct(self):
        name = self.fieldName.text()
        brand = self.fieldBrand.currentText()
        category = self.fieldCategory.currentText()
        stock = self.fieldStock.text()
        prize = self.fieldPrize.text()
        # some validations for the inputs
        if name == '' or len(name) <= 5:
            self.showMessage('Input Error', 'Please enter valid name')
            return
        if name in self.inv.getAllProductNames():
            self.showMessage('Input Error', 'Product already exists!')
            return
        if brand == 'select':
            self.showMessage('Input Error', 'Please select a brand')
            return
        if category == 'select':
            self.showMessage('Input Error', 'Please select a category')
            return
        if prize == '' or prize == 0:
            self.showMessage('Input Error', 'Please enter valid prize')
            return
        if stock == '':
            self.showMessage('Input Error', 'Please enter valid stock')
            return

        stock = int(stock)
        prize = float(prize)
        self.inv.addProduct(name, brand, category, stock, prize)

    def addBrand(self):
        brand = self.fieldNewBrand.text()
        # some validations for the input
        if brand == '':
            self.showMessage('Input Error', 'Please enter valid brand name')
            return
        self.inv.addBrand(brand)

    def addCategory(self):
        category = self.fieldNewBrand.text()
        # some validations for the input
        if category == '':
            self.showMessage('Input Error', 'Please enter valid category name')
            return
        self.inv.addCategory(category)

    def showMessage(self, title, message):
        msg = QMessageBox()
        msg.about(self.widget, title, message)


class UIPurchase(Ui_purchase):
    def __init__(self, widget, crt, inv):
        self.widget = widget
        self.crt = crt
        self.inv = inv
        self.setupUi(widget)
        # initialize combobox
        self.fieldBrand.addItem('select')
        self.fieldBrand.addItems(self.inv.getAllBrandNames())
        self.fieldCategory.addItem('select')
        self.fieldCategory.addItems(self.inv.getAllCategoryNames())
        self.fieldName.addItem('select')
        self.fieldName.addItems(self.inv.getAllProductNames())
        # event updates
        self.buttonClear.clicked.connect(lambda: self.clear())
        self.buttonAdd.clicked.connect(lambda: self.AddToCart())
        self.fieldCategory.currentIndexChanged.connect(lambda: self.updateProductField())
        self.fieldBrand.currentIndexChanged.connect(lambda: self.updateProductField())

    def clear(self):
        self.fieldCode.setValue(0)
        self.fieldUnits.setValue(0)
        self.fieldName.clear()
        self.fieldName.addItem('select')
        self.fieldName.addItems(self.inv.getAllProductNames())
        self.fieldCategory.setCurrentIndex(0)
        self.fieldBrand.setCurrentIndex(0)

    def AddToCart(self):
        units = self.fieldUnits.text()
        productCode = self.fieldCode.text()
        if productCode == '' or productCode == '0':
            self.showMessage('Input Error', 'Please select a product')
            return
        if units == '0':
            self.showMessage('Input Error', 'Please set the units required')
            return
        units = int(units)
        productCode = int(productCode)
        self.crt.newProduct(productCode, units)

    def updateProductField(self):
        """method to update the items of the fieldname based on the update in other fields"""
        if self.fieldBrand.currentText() == 'select' and self.fieldCategory.currentText() == 'select':
            self.inv.getAllProductNames()
        elif self.fieldBrand.currentText() == 'select':
            self.inv.getAllProductNames(brandId=None, categoryId=self.fieldCategory.currentText())
        elif self.fieldCategory.currentText() == 'select':
            self.inv.getAllProductNames(brandId=self.fieldBrand)

    def showMessage(self, title, message):
        msg = QMessageBox()
        msg.about(self.widget, title, message)


class UISuperMarket(QMainWindow):
    def __init__(self):
        super().__init__()
        # setup the mainwindow
        self.resize(800, 600)
        self.setWindowTitle('MASS Supermarket')
        self.setWindowIcon(QIcon('res/images/icon.png'))
        self.centralwidget = QStackedWidget(self)
        self.setCentralWidget(self.centralwidget)
        self.setContentsMargins(0, 20, 0, 0)

        self.crt = Cart()
        self.inv = Inventory()

        # setup contents of stacked widget
        self.purchaseWidget = QWidget()
        UIPurchase(self.purchaseWidget, self.crt, self.inv)
        self.centralwidget.addWidget(self.purchaseWidget)
        self.addWidget = QWidget()
        UIProducts(self.addWidget, self.crt, self.inv)
        self.centralwidget.addWidget(self.addWidget)

        # set the widget that should be shown at first
        self.setWidget(self.purchaseWidget)
        self.setupMenuBar()
        self.show()

    def setWidget(self, widget):
        """method to set the active widget in the stacked widget"""
        self.centralwidget.setCurrentWidget(widget)

    def setupMenuBar(self):
        """method to setup the menubar"""
        menubar = QMenuBar(self)
        menubar.setGeometry(QRect(0, 0, 5000, 20))
        purchase = menubar.addAction('Purchase')
        products = menubar.addAction('Products')
        updateStock = menubar.addAction('Update Stock')
        ViewStock = menubar.addAction('Stock')

        purchase.triggered.connect(lambda: self.setWidget(self.purchaseWidget))
        products.triggered.connect(lambda: self.setWidget(self.addWidget))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = UISuperMarket()
    sys.exit(app.exec_())
