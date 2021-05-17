import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QApplication, QMenuBar, QMainWindow, QStackedWidget, QWidget

from superMarket import Cart, Inventory
from ui.purchase import Ui_purchase


class UISuperMarket(QMainWindow):
    def __init__(self):
        super().__init__()

        self.resize(800, 600)
        self.setWindowTitle('MASS Supermarket')
        self.setWindowIcon(QIcon('res/images/icon.png'))
        self.centralWidget = QStackedWidget(self)
        self.setCentralWidget(self.centralWidget)

        self.purchaseWidget = QWidget()
        Purchase(self.purchaseWidget)
        self.centralWidget.addWidget(self.purchaseWidget)

        self.centralWidget.setCurrentWidget(self.purchaseWidget)
        self.setupMenuBar()
        self.show()

    def setupMenuBar(self):
        menubar = QMenuBar(self)
        menubar.setGeometry(QRect(0, 0, 5000, 20))
        purchase = menubar.addMenu('Purchase')
        newProduct = menubar.addMenu('New Product')
        updateStock = menubar.addMenu('Update Stock')
        ViewStock = menubar.addMenu('Stock')


class Purchase(Ui_purchase):
    def __init__(self, widget):
        super().__init__()
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
        self.buttonClear.clicked.connect(self.clear)
        self.buttonAdd.clicked.connect(self.AddToCart)
        self.fieldCategory.currentIndexChanged.connect(self.updateProductNames)
        self.fieldBrand.currentIndexChanged.connect(self.updateProductNames)

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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = UISuperMarket()
    sys.exit(app.exec_())
