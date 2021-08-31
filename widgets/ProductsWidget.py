import re

from PySide6.QtGui import Qt, QDoubleValidator
from PySide6.QtWidgets import QWidget, QHeaderView, QTableWidgetItem

from SuperMarket import Products
from widgets.UIFunctions import showMessage, showDialog, askQuestion
from ui.products import Ui_products


class ProductsWidget(QWidget, Ui_products):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.setAttribute(Qt.WA_StyledBackground, True)

        self.products = Products()
        self.fieldPrize.setValidator(QDoubleValidator(0, 10000, 2))

        # initialize combobox
        self.fieldBrand.addItem('select')
        self.fieldBrand.addItems(self.products.getBrandsData(b_id=False, name=True))
        self.fieldCategory.addItem('select')
        self.fieldCategory.addItems(self.products.getCategoriesData(c_id=False, name=True))
        # event updates
        self.buttonClear.clicked.connect(lambda: self.clear())
        self.buttonAddProduct.clicked.connect(lambda: self.addProduct())
        self.buttonAddBrand.clicked.connect(lambda: self.addBrand())
        self.buttonAddCategory.clicked.connect(lambda: self.addCategory())
        self.buttonDeleteProduct.clicked.connect(lambda: self.deleteProduct())
        self.buttonDeleteBrand.clicked.connect(lambda: self.deleteBrand())
        self.buttonDeleteCategory.clicked.connect(lambda: self.deleteCategory())
        self.buttonUpdateProduct.clicked.connect(lambda: self.updateProduct())
        self.buttonUpdateBrand.clicked.connect(lambda: self.updateBrand())
        self.buttonUpdateCategory.clicked.connect(lambda: self.updateCategory())

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
        for i, row in enumerate(data):
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
        self.fieldCategory.addItems(self.products.getCategoriesData(c_id=False, name=True))

        self.fieldBrand.clear()
        self.fieldBrand.addItem('select')
        self.fieldBrand.addItems(self.products.getBrandsData(b_id=False, name=True))

    def addProduct(self):
        name = self.fieldName.text()
        brand = self.fieldBrand.currentText()
        category = self.fieldCategory.currentText()
        stock = self.fieldStock.text()
        prize = self.fieldPrize.text()

        name_regex = re.compile(r'[A-Za-z0-9_\s\-.]{5,30}')
        # some validations for the inputs
        if not name_regex.fullmatch(name):
            showMessage(self, 'Input Error', 'Please enter valid name')
            return
        if name in self.products.getProductsData(name=True):
            showMessage(self, 'Input Error', 'Product already exists!')
            return
        if brand == 'select':
            showMessage(self, 'Input Error', 'Please select a brand')
            return
        if category == 'select':
            showMessage(self, 'Input Error', 'Please select a category')
            return
        if prize == '' or prize == 0 or not prize.isdigit():
            showMessage(self, 'Input Error', 'Please enter valid prize')
            return
        if stock == '' or not stock.isdigit():
            showMessage(self, 'Input Error', 'Please enter valid stock')
            return

        stock = int(stock)
        prize = float(prize)
        category = self.products.getCategoryId(category)
        brand = self.products.getBrandId(brand)
        self.products.addProduct(name, brand, category, stock, prize)
        self.setProductsTableData()
        self.clear()
        showMessage(self, 'Product added', name + ' added to products successfully')

    def addBrand(self):
        brand = self.fieldNewBrand.text()
        # some validations for the input
        name_regex = re.compile(r'[A-Za-z0-9_\s\-.]{1,20}')

        if not name_regex.fullmatch(brand):
            showMessage(self, 'Input Error', 'Please enter valid brand name')
            return
        if brand in self.products.getBrandsData(b_id=False, name=True):
            showMessage(self, 'Input Error', 'Brand already exists!')
            return
        self.products.addBrand(brand)
        self.fieldNewBrand.clear()
        self.setBrandTableData()
        self.clear()
        showMessage(self, 'Brand added', brand + ' added to brands successfully')

    def addCategory(self):
        category = self.fieldNewCategory.text()
        name_regex = re.compile(r'[A-Za-z0-9_\s\-.]{1,20}')

        if not name_regex.fullmatch(category):
            showMessage(self, 'Input Error', 'Please enter valid category name')
            return
        if category in self.products.getCategoriesData(c_id=False, name=True):
            showMessage(self, 'Input Error', 'Category already exists!')
            return
        self.products.addCategory(category)
        self.fieldNewCategory.clear()
        self.setCategoryTableData()
        self.clear()
        showMessage(self, 'Category added', category + ' added to categories successfully')

    def deleteProduct(self):
        if not self.tableProducts.selectedItems():
            showMessage(self, 'Error', 'Please select a product')
        else:
            p_id = self.tableProducts.selectedItems()[0].text()
            p_name = self.tableProducts.selectedItems()[1].text()
            x = askQuestion(self, 'Deletion Warning',
                            'Do you really want to delete the product ' + p_name + '?')
            if x:
                self.products.deleteProduct(p_id)
                self.setProductsTableData()

    def deleteBrand(self):
        if not self.tableBrands.selectedItems():
            showMessage(self, 'Error', 'Please select a brand')
        else:
            b_id = self.tableBrands.selectedItems()[0].text()
            b_name = self.tableBrands.selectedItems()[1].text()
            x = askQuestion(self, 'Deletion Warning', 'Do you really want to delete the brand ' + b_name + '?')
            if x:
                if self.products.isDeletableBrand(b_id):
                    self.products.deleteBrand(b_id)
                    self.setBrandTableData()
                else:
                    showMessage(self, 'Deletion Error',
                                'Some products exists with this brand!. You can only update the brand name until '
                                'the products exist.')

    def deleteCategory(self):
        if not self.tableCategories.selectedItems():
            showMessage(self, 'Error', 'Please select a category')
        else:
            c_id = self.tableCategories.selectedItems()[0].text()
            c_name = self.tableCategories.selectedItems()[1].text()
            x = askQuestion(self, 'Deletion Warning',
                            'Do you really want to delete the category ' + c_name + '?')
            if x:
                if self.products.isDeletableCategory(c_id):
                    self.products.deleteCategory(c_id)
                    self.setCategoryTableData()
                else:
                    showMessage(self, 'Deletion Error',
                                'Some products exists with this category!. You can only update the category name '
                                'until the products exist.')

    def updateProduct(self):
        if not self.tableProducts.selectedItems():
            showMessage(self, 'Error', 'Please select a product')
        else:
            p_id = self.tableProducts.selectedItems()[0].text()
            name = showDialog(self, 'Update Product Name', 'Enter modified product name')
            name_regex = re.compile(r'[A-Za-z0-9_\s\-.]{5,30}')
            # some validations for the inputs
            if not name_regex.fullmatch(name):
                showMessage(self, 'Input Error', 'Please enter valid name')
                return
            if name:
                self.products.updateProduct(p_id, name)
                self.setProductsTableData()

    def updateBrand(self):
        if not self.tableBrands.selectedItems():
            showMessage(self, 'Error', 'Please select a brand')
        else:
            b_id = self.tableBrands.selectedItems()[0].text()
            name = showDialog(self, 'Update Brand Name', 'Enter modified brand name')
            name_regex = re.compile(r'[A-Za-z0-9_\s\-.]{1,20}')

            if not name_regex.fullmatch(name):
                showMessage(self, 'Input Error', 'Please enter valid brand name')
                return
            if name:
                self.products.updateBrand(b_id, name)
                self.setBrandTableData()

    def updateCategory(self):
        if not self.tableCategories.selectedItems():
            showMessage(self, 'Error', 'Please select a category')
        else:
            p_id = self.tableCategories.selectedItems()[0].text()
            name = showDialog(self, 'Update category Name', 'Enter modified category name')
            name_regex = re.compile(r'[A-Za-z0-9_\-.]{1,20}')

            if not name_regex.fullmatch(name):
                showMessage(self, 'Input Error', 'Please enter valid brand name')
                return
            if name:
                self.products.updateCategory(p_id, name)
                self.setCategoryTableData()
