import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QApplication, QMenuBar, QMainWindow, QStackedWidget, QWidget

from superMarket import Cart, Inventory

from ui.addProduct import Ui_newProduct
from ui.purchase import Ui_purchase


class AddProduct(Ui_newProduct):
    def __init__(self, widget):
        self.setupUi(widget)


class Purchase(Ui_purchase):
    def __init__(self, widget):
        self.crt = Cart()
        self.inv = Inventory()
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
        self.fieldCategory.currentIndexChanged.connect(lambda: self.updateProductNames())
        self.fieldBrand.currentIndexChanged.connect(lambda: self.updateProductNames())

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


class UISuperMarket(QMainWindow):
    def __init__(self):
        super().__init__()

        self.resize(800, 600)
        self.setWindowTitle('MASS Supermarket')
        self.setWindowIcon(QIcon('res/images/icon.png'))
        self.centralwidget = QStackedWidget(self)
        self.setCentralWidget(self.centralwidget)

        # setup contents of stacked widget
        self.purchaseWidget = QWidget()
        Purchase(self.purchaseWidget)
        self.centralwidget.addWidget(self.purchaseWidget)

        self.addWidget = QWidget()
        AddProduct(self.addWidget)
        self.centralwidget.addWidget(self.addWidget)

        self.setWidget(self.purchaseWidget)
        self.setupMenuBar()
        self.setContentsMargins(0,20,0,0)
        self.show()

    def setWidget(self, widget):
        self.centralwidget.setCurrentWidget(widget)

    def setupMenuBar(self):
        menubar = QMenuBar(self)
        menubar.setGeometry(QRect(0, 0, 5000, 20))
        purchase = menubar.addAction('Purchase')
        newProduct = menubar.addAction('New Product')
        updateStock = menubar.addAction('Update Stock')
        ViewStock = menubar.addAction('Stock')

        purchase.triggered.connect(lambda: self.setWidget(self.purchaseWidget))
        newProduct.triggered.connect(lambda: self.setWidget(self.addWidget))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = UISuperMarket()
    sys.exit(app.exec_())
