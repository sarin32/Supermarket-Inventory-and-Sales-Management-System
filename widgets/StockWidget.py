from PySide6.QtGui import Qt
from PySide6.QtWidgets import QWidget, QHeaderView, QTableWidgetItem

from SuperMarket import Products
from widgets.UIFunctions import showMessage, showDialog
from ui.stock import Ui_stock


class StockWidget(QWidget, Ui_stock):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.setAttribute(Qt.WA_StyledBackground, True)

        self.products = Products()

        # initialize combobox
        self.fieldBrand.addItem('select')
        self.fieldBrand.addItems(self.products.getBrandsData(b_id=False, name=True))
        self.fieldCategory.addItem('select')
        self.fieldCategory.addItems(self.products.getCategoriesData(c_id=False, name=True))

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
        self.fieldBrand.addItems(self.products.getBrandsData(b_id=False, name=True))

        self.fieldCategory.clear()
        self.fieldCategory.addItem('select')
        self.fieldCategory.addItems(self.products.getCategoriesData(c_id=False, name=True))

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
        data = self.products.getProductsData(True, True, True, True, True, True, filterBrand, filterCategory,
                                             filterType)
        for i, row in enumerate(data):
            self.tableStock.insertRow(i)
            for j, item in enumerate(row):
                newItem = QTableWidgetItem(item)
                self.tableStock.setItem(i, j, newItem)

    def updateStock(self):
        if not self.tableStock.selectedItems():
            showMessage(self, 'Error', 'Please select a product')
        else:
            p_id = self.tableStock.selectedItems()[0].text()
            try:
                stock = int(showDialog(self, 'Update Stock', 'Enter number of new stock units'))
            except ValueError:
                showMessage(self, 'Input Error', 'invalid number of units')
                return
            if stock:
                self.products.updateStock(p_id, stock)
                self.loadStock()

    def updatePrize(self):
        if not self.tableStock.selectedItems():
            showMessage(self, 'Error', 'Please select a product')
        else:
            p_id = self.tableStock.selectedItems()[0].text()
            try:
                prize = float(showDialog(self, 'Update Prize', 'Enter new prize in rupees'))
            except ValueError:
                showMessage(self, 'Input Error', 'invalid prize')
                return
            except TypeError:
                return
            if prize:
                self.products.updatePrize(p_id, prize)
                self.loadStock()
