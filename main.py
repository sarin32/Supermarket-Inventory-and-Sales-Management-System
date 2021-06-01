"""
This is the runner file of the application
Mainwindow is created and other widgets are added in this file
"""
import sys
from datetime import datetime

from PyQt5.QtCore import QFile, QRect, QTextStream
from PyQt5.QtGui import QDoubleValidator, QIcon
from PyQt5.QtWidgets import *

from cart import Cart
from products import Products
from sales import Sales
from ui.products import Ui_products
from ui.purchase import Ui_purchase
from ui.sales import Ui_sales
from ui.stock import Ui_stock


class UIProducts(Ui_products):
    def __init__(self, widget):
        self.widget = widget
        self.products = Products()
        self.setupUi(widget)
        self.fieldPrize.setValidator(QDoubleValidator(0, 10000, 2))
        # initialize combobox
        self.fieldBrand.addItem('select')
        self.fieldBrand.addItems(
            self.products.getBrandsData(b_id=False, name=True))
        self.fieldCategory.addItem('select')
        self.fieldCategory.addItems(
            self.products.getCategoriesData(c_id=False, name=True))
        # event updates
        self.buttonClear.clicked.connect(lambda: self.clear())
        self.buttonAddProduct.clicked.connect(lambda: self.addProduct())
        self.buttonAddBrand.clicked.connect(lambda: self.addBrand())
        self.buttonAddCategory.clicked.connect(lambda: self.addCategory())
        self.buttonDeleteProduct.clicked.connect(lambda: self.deleteProduct())
        self.buttonDeleteBrand.clicked.connect(lambda: self.deleteBrand())
        self.buttonDeleteCategory.clicked.connect(
            lambda: self.deleteCategory())
        self.buttonUpdateProduct.clicked.connect(lambda: self.updateProduct())
        self.buttonUpdateBrand.clicked.connect(lambda: self.updateBrand())
        self.buttonUpdateCategory.clicked.connect(
            lambda: self.updateCategory())

        # setup tables
        header = self.tableBrands.horizontalHeader()
        header.setSectionResizeMode(1, QHeaderView.Stretch)
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.setBrandTableData()

        header = self.tableCategories.horizontalHeader()
        header.setSectionResizeMode(1, QHeaderView.Stretch)
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.setCategoryTableData()

        header = self.tableProducts.horizontalHeader()
        header.setSectionResizeMode(1, QHeaderView.Stretch)
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.setProductsTableData()

    def setBrandTableData(self):
        self.tableBrands.setRowCount(0)
        data = self.products.getBrandsData(b_id=True, name=True)
        for i, row in enumerate(data):
            self.tableBrands.insertRow(i)
            for j, item in enumerate(row):
                newItem = QTableWidgetItem(item)
                self.tableBrands.setItem(i, j, newItem)

    def setCategoryTableData(self):
        self.tableCategories.setRowCount(0)
        data = self.products.getCategoriesData(c_id=True, name=True)
            self.tableCategories.insertRow(i)
            for j, item in enumerate(row):
                newItem = QTableWidgetItem(item)
                self.tableCategories.setItem(i, j, newItem)

    def setProductsTableData(self):
        self.tableProducts.setRowCount(0)
        data = self.products.getProductsData(True, True)
        for i, row in enumerate(data):
            self.tableProducts.insertRow(i)
            for j, item in enumerate(row):
                newItem = QTableWidgetItem(item)
                self.tableProducts.setItem(i, j, newItem)

    def clear(self):
        self.fieldPrize.clear()
        self.fieldStock.setValue(0)
        self.fieldName.clear()

        self.fieldCategory.clear()
        self.fieldCategory.addItem('select')
        self.fieldCategory.addItems(
            self.products.getCategoriesData(c_id=False, name=True))

        self.fieldBrand.clear()
        self.fieldBrand.addItem('select')
        self.fieldBrand.addItems(
            self.products.getBrandsData(b_id=False, name=True))

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
        if name in self.products.getProductsData(name=True):
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
        category = self.products.getCategoryId(category)
        brand = self.products.getBrandId(brand)
        self.products.addProduct(name, brand, category, stock, prize)
        self.setProductsTableData()
        self.clear()
        self.showMessage('Product added',
                         name + ' added to products successfully')

    def addBrand(self):
        brand = self.fieldNewBrand.text()
        # some validations for the input
        if brand == '':
            self.showMessage('Input Error', 'Please enter valid brand name')
            return
        if brand in self.products.getBrandsData(b_id=False, name=True):
            self.showMessage('Input Error', 'Brand already exists!')
            return
        self.products.addBrand(brand)
        self.fieldNewBrand.clear()
        self.setBrandTableData()
        self.clear()
        self.showMessage('Brand added',
                         brand + ' added to brands successfully')

    def addCategory(self):
        category = self.fieldNewCategory.text()
        # some validations for the input
        if category == '':
            self.showMessage('Input Error', 'Please enter valid category name')
            return
        if category in self.products.getCategoriesData(c_id=False, name=True):
            self.showMessage('Input Error', 'Category already exists!')
            return
        self.products.addCategory(category)
        self.fieldNewCategory.clear()
        self.setCategoryTableData()
        self.clear()
        self.showMessage('Category added',
                         category + ' added to categories successfully')

    def deleteProduct(self):
        if not self.tableProducts.selectedItems():
            self.showMessage('Error', 'Please select a product')
        else:
            p_id = self.tableProducts.selectedItems()[0].text()
            p_name = self.tableProducts.selectedItems()[1].text()
            x = self.askQuestion(
                'Deletion Warning',
                'Do you really want to delete the product ' + p_name + '?')
            if x:
                self.products.deleteProduct(p_id)
                self.setProductsTableData()

    def deleteBrand(self):
        if not self.tableBrands.selectedItems():
            self.showMessage('Error', 'Please select a brand')
        else:
            b_id = self.tableBrands.selectedItems()[0].text()
            b_name = self.tableBrands.selectedItems()[1].text()
            x = self.askQuestion(
                'Deletion Warning',
                'Do you really want to delete the brand ' + b_name + '?')
            if x:
                if self.products.isDeletableBrand(b_id):
                    self.products.deleteBrand(b_id)
                    self.setBrandTableData()
                else:
                    self.showMessage(
                        'Deletion Error',
                        'Some products exists with this brand!. You can only update the brand name until '
                        'the products exist.')

    def deleteCategory(self):
        if not self.tableCategories.selectedItems():
            self.showMessage('Error', 'Please select a category')
        else:
            c_id = self.tableCategories.selectedItems()[0].text()
            c_name = self.tableCategories.selectedItems()[1].text()
            x = self.askQuestion(
                'Deletion Warning',
                'Do you really want to delete the category ' + c_name + '?')
            if x:
                if self.products.isDeletableCategory(c_id):
                    self.products.deleteCategory(c_id)
                    self.setCategoryTableData()
                else:
                    self.showMessage(
                        'Deletion Error',
                        'Some products exists with this category!. You can only update the category name '
                        'until the products exist.')

    def updateProduct(self):
        if not self.tableProducts.selectedItems():
            self.showMessage('Error', 'Please select a product')
        else:
            p_id = self.tableProducts.selectedItems()[0].text()
            name = self.showDialog('Update Product Name',
                                   'Enter modified product name')
            if name:
                self.products.updateProduct(p_id, name)
                self.setProductsTableData()

    def updateBrand(self):
        if not self.tableBrands.selectedItems():
            self.showMessage('Error', 'Please select a brand')
        else:
            b_id = self.tableBrands.selectedItems()[0].text()
            name = self.showDialog('Update Brand Name',
                                   'Enter modified brand name')
            if name:
                self.products.updateBrand(b_id, name)
                self.setBrandTableData()

    def updateCategory(self):
        if not self.tableCategories.selectedItems():
            self.showMessage('Error', 'Please select a category')
        else:
            p_id = self.tableCategories.selectedItems()[0].text()
            name = self.showDialog('Update category Name',
                                   'Enter modified category name')
            if name:
                self.products.updateCategory(p_id, name)
                self.setCategoryTableData()

    def showMessage(self, title, message):
        msg = QMessageBox()
        msg.about(self.widget, title, message)

    def askQuestion(self, title, message):
        buttonReply = QMessageBox.question(self.widget, title, message,
                                           QMessageBox.Yes | QMessageBox.No,
                                           QMessageBox.No)
        if buttonReply == QMessageBox.Yes:
            return True
        return False

    def showDialog(self, title, message):
        text, ok = QInputDialog.getText(self.widget, title, message)
        if ok:
            return text


class UIPurchase(Ui_purchase):
    def __init__(self, widget):
        self.widget = widget
        self.crt = Cart()
        self.setupUi(widget)
        # initialize combobox
        self.fieldBrand.addItem('select')
        self.fieldBrand.addItems(self.crt.getBrandsData(b_id=False, name=True))
        self.fieldCategory.addItem('select')
        self.fieldCategory.addItems(
            self.crt.getCategoriesData(c_id=False, name=True))
        self.fieldName.addItem('select')
        self.fieldName.addItems(self.crt.getProductsData(name=True))
        # event updates
        self.buttonClear.clicked.connect(lambda: self.clear())
        self.buttonAdd.clicked.connect(lambda: self.AddToCart())
        self.buttonRemove.clicked.connect(lambda: self.removeProduct())
        self.buttonClearAll.clicked.connect(lambda: self.clearCart())
        self.buttonPurchase.clicked.connect(lambda: self.purchase())
        self.fieldCategory.activated.connect(lambda: self.updateProductField())
        self.fieldBrand.activated.connect(lambda: self.updateProductField())
        self.fieldCode.returnPressed.connect(lambda: self.productCodeChange())
        self.fieldName.activated.connect(lambda: self.productNameChange())

        # setup tables
        header = self.tableCart.horizontalHeader()
        header.setSectionResizeMode(1, QHeaderView.Stretch)
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(4, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(5, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(6, QHeaderView.ResizeToContents)
        self.setupCartTable()

    def clear(self):
        """method to clears and resets all input fields"""
        self.fieldCode.clear()
        self.fieldUnits.setValue(0)

        self.fieldBrand.clear()
        self.fieldBrand.addItem('select')
        self.fieldBrand.addItems(self.crt.getBrandsData(b_id=False, name=True))

        self.fieldCategory.clear()
        self.fieldCategory.addItem('select')
        self.fieldCategory.addItems(
            self.crt.getCategoriesData(c_id=False, name=True))

        self.fieldName.clear()
        self.fieldName.addItem('select')
        self.fieldName.addItems(self.crt.getProductsData(name=True))

    def AddToCart(self):
        """method to add items to the cart"""
        units = self.fieldUnits.text()
        productCode = self.fieldCode.text()
        if productCode == '' or productCode == '0':
            self.showMessage('Input Error', 'Please select a product')
            return
        if units == '0':
            self.showMessage('Input Error', 'Please set the units required')
            return
        if self.crt.isExistingProduct(int(productCode)):
            self.showMessage('Input Error', 'Product already Exist in cart!')
            return
        if int(self.crt.getProductDetails(productCode)[4]) < int(units):
            self.showMessage('Input Error',
                             units + ' units of product is not available!')
            return
        units = int(units)
        productCode = int(productCode)
        self.crt.newProduct(productCode, units)
        self.clear()
        self.setupCartTable()
        self.updateTotalCost()

    def updateProductField(self):
        """method to update the items of the fieldname and fieldCode based on the update in fieldBrand fieldCategory"""
        self.fieldCode.clear()
        self.fieldName.clear()
        self.fieldName.addItem('select')
        brand = None
        category = None
        if self.fieldBrand.currentIndex() != 0:
            brand = self.fieldBrand.currentText()
        if self.fieldCategory.currentIndex() != 0:
            category = self.fieldCategory.currentText()
        self.fieldName.addItems(
            self.crt.getProductsData(name=True,
                                     filterBrand=brand,
                                     filterCategory=category))

    def productCodeChange(self):
        """method to update all other fields when fieldCode is changed by user"""
        code = self.fieldCode.text()
        if code != '':
            details = self.crt.getProductDetails(code)
            if details is not None:
                name = details[1]
                brand = details[2]
                category = details[3]
                self.fieldBrand.setCurrentText(brand)
                self.fieldCategory.setCurrentText(category)
                self.fieldName.clear()
                self.fieldName.addItem('select')
                self.fieldName.addItems(
                    self.crt.getProductsData(name=True,
                                             filterBrand=brand,
                                             filterCategory=category))
                self.fieldName.setCurrentText(name)
            else:
                self.fieldCode.clear()
                self.showMessage('Input Error',
                                 'No product found with product code ' + code)

    def productNameChange(self):
        """method to update all other fields when fieldName is changed by user"""
        if self.fieldName.currentText() == 'select':
            self.clear()
            return
        code = self.crt.getProductId(self.fieldName.currentText())
        details = self.crt.getProductDetails(code)
        name = details[1]
        brand = details[2]
        category = details[3]
        self.fieldBrand.setCurrentText(brand)
        self.fieldCategory.setCurrentText(category)
        self.fieldCode.setText(code)
        self.fieldName.clear()
        self.fieldName.addItem('select')
        self.fieldName.addItems(
            self.crt.getProductsData(name=True,
                                     filterBrand=brand,
                                     filterCategory=category))
        self.fieldName.setCurrentText(name)

    def showMessage(self, title, message):
        """method to show any message to the user with a title and description"""
        msg = QMessageBox()
        msg.about(self.widget, title, message)

    def setupCartTable(self):
        data = self.crt.getCartTable()
        self.tableCart.setRowCount(0)
        for i, row in enumerate(data):
            self.tableCart.insertRow(i)
            for j, item in enumerate(row):
                newItem = QTableWidgetItem(item)
                self.tableCart.setItem(i, j, newItem)

    def updateTotalCost(self):
        total = self.crt.getTotalCost()
        self.labelCost.setText(str(total))

    def clearCart(self):
        self.crt.clearCart()
        self.setupCartTable()

    def removeProduct(self):
        if not self.tableCart.selectedItems():
            self.showMessage('Error', 'Please select a brand')
        else:
            p_id = int(self.tableCart.selectedItems()[0].text())
            self.crt.removeProduct(p_id)
            self.setupCartTable()

    def purchase(self):
        if self.tableCart.rowCount() == 0:
            self.showMessage('Error', 'No item in cart')
            return
        x = self.askQuestion('Purchase Warning', 'Confirm Purchase?')
        if x:
            self.crt.makePurchase()
            self.clearCart()

    def askQuestion(self, title, message):
        buttonReply = QMessageBox.question(self.widget, title, message,
                                           QMessageBox.Yes | QMessageBox.No,
                                           QMessageBox.No)
        if buttonReply == QMessageBox.Yes:
            return True
        return False


class UIStock(Ui_stock):
    def __init__(self, widget):
        self.widget = widget
        self.products = Products()
        self.setupUi(widget)

        # initialize combobox
        self.fieldBrand.addItem('select')
        self.fieldBrand.addItems(
            self.products.getBrandsData(b_id=False, name=True))
        self.fieldCategory.addItem('select')
        self.fieldCategory.addItems(
            self.products.getCategoriesData(c_id=False, name=True))

        # event updates
        self.buttonClear.clicked.connect(lambda: self.clear())
        self.buttonLoad.clicked.connect(lambda: self.loadStock())
        self.buttonUpdateStock.clicked.connect(lambda: self.updateStock())
        self.buttonUpdatePrize.clicked.connect(lambda: self.updatePrize())

        # setup tables
        header = self.tableStock.horizontalHeader()
        header.setSectionResizeMode(1, QHeaderView.Stretch)
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(4, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(5, QHeaderView.ResizeToContents)
        # self.loadStock()

    def clear(self):
        self.fieldBrand.clear()
        self.fieldBrand.addItem('select')
        self.fieldBrand.addItems(
            self.products.getBrandsData(b_id=False, name=True))

        self.fieldCategory.clear()
        self.fieldCategory.addItem('select')
        self.fieldCategory.addItems(
            self.products.getCategoriesData(c_id=False, name=True))

        self.fieldType.setCurrentIndex(0)

    def loadStock(self):
        filterBrand = None
        filterCategory = None
        filterType = None
        if self.fieldBrand.currentIndex() != 0:
            filterBrand = self.fieldBrand.currentText()
        if self.fieldCategory.currentIndex() != 0:
            filterCategory = self.fieldCategory.currentText()
        x = self.fieldType.currentIndex()
        if x == 1:
            filterType = self.products.INSTOCK
        if x == 2:
            filterType = self.products.OUTSTOCK
        self.tableStock.setRowCount(0)
        data = self.products.getProductsData(True, True, True, True, True,
                                             True, filterBrand, filterCategory,
                                             filterType)
        for i, row in enumerate(data):
            self.tableStock.insertRow(i)
            for j, item in enumerate(row):
                newItem = QTableWidgetItem(item)
                self.tableStock.setItem(i, j, newItem)

    def updateStock(self):
        if not self.tableStock.selectedItems():
            self.showMessage('Error', 'Please select a product')
        else:
            p_id = self.tableStock.selectedItems()[0].text()
            try:
                stock = int(
                    self.showDialog('Update Stock',
                                    'Enter number of new stock units'))
            except ValueError:
                self.showMessage('Input Error', 'invalid number of units')
                return
            if stock:
                self.products.updateStock(p_id, stock)
                self.loadStock()

    def updatePrize(self):
        if not self.tableStock.selectedItems():
            self.showMessage('Error', 'Please select a product')
        else:
            p_id = self.tableStock.selectedItems()[0].text()
            try:
                prize = float(
                    self.showDialog('Update Prize',
                                    'Enter new prize in rupees'))
            except ValueError:
                self.showMessage('Input Error', 'invalid prize')
                return
            except TypeError:
                return
            if prize:
                self.products.updatePrize(p_id, prize)
                self.loadStock()

    def showMessage(self, title, message):
        msg = QMessageBox()
        msg.about(self.widget, title, message)

    def showDialog(self, title, message):
        text, ok = QInputDialog.getText(self.widget, title, message)
        if ok:
            return text
        return None


class UISales(Ui_sales):
    def __init__(self, widget):
        self.widget = widget
        self.sale = Sales()
        self.setupUi(widget)

        self.buttonCheck.clicked.connect(lambda: self.check())
        self.buttonLoad.clicked.connect(lambda: self.setupSalesTableData())

        # setup tables
        header = self.tableSales.horizontalHeader()
        header.setSectionResizeMode(1, QHeaderView.Stretch)
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QHeaderView.ResizeToContents)
        self.setupSalesTableData()

        # setup year field
        start = 2018
        end = datetime.now().year
        for year in range(end, start, -1):
            self.fieldYear.addItem(str(year))

    def check(self):
        month = self.fieldMonth.currentIndex() + 1
        year = int(self.fieldYear.currentText())
        amount = self.sale.getMonthlySaleAmount(month, year)
        self.labelMonthlyAmount.setText(str(float(amount)))

    def showMessage(self, title, message):
        """method to show any message to the user with a title and description"""
        msg = QMessageBox()
        msg.about(self.widget, title, message)

    def setupSalesTableData(self):
        self.tableSales.setRowCount(0)
        date = self.calendar.selectedDate()
        pydate = str(date.toPyDate())
        data = self.sale.getSalesDetails(pydate)
        total = self.sale.getTotalSaleAmount()
        if not data:
            self.showMessage('Information', 'No sales at specified date')
        for i, row in enumerate(data):
            self.tableSales.insertRow(i)
            for j, item in enumerate(row):
                newItem = QTableWidgetItem(item)
                self.tableSales.setItem(i, j, newItem)
        self.labeldailyAmount.setText(str(total))


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

        file = QFile('stylesheets/main.qss')
        if not file.open(QFile.ReadOnly | QFile.Text):
            raise Exception("FileNotFound")
        qss = QTextStream(file)
        self.setStyleSheet(qss.readAll())

        # setup contents of stacked widget
        self.purchaseWidget = QWidget()
        UIPurchase(self.purchaseWidget)
        self.centralwidget.addWidget(self.purchaseWidget)

        self.productsWidget = QWidget()
        UIProducts(self.productsWidget)
        self.centralwidget.addWidget(self.productsWidget)

        self.stockWidget = QWidget()
        UIStock(self.stockWidget)
        self.centralwidget.addWidget(self.stockWidget)

        self.salesWidget = QWidget()
        UISales(self.salesWidget)
        self.centralwidget.addWidget(self.salesWidget)

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
        stock = menubar.addAction('Stock')
        sales = menubar.addAction('Sales')

        purchase.triggered.connect(lambda: self.setWidget(self.purchaseWidget))
        products.triggered.connect(lambda: self.setWidget(self.productsWidget))
        stock.triggered.connect(lambda: self.setWidget(self.stockWidget))
        sales.triggered.connect(lambda: self.setWidget(self.salesWidget))


# runner
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = UISuperMarket()
    sys.exit(app.exec_())

    # setup stylesheet
