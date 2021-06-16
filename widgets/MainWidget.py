import json

from PySide6.QtCore import QFile, QTextStream, QRect
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QMainWindow, QStackedWidget, QMenuBar

from widgets.ProductsWidget import UIProducts
from widgets.PurchaseWidget import UIPurchase
from widgets.SalesWidget import UISales
from widgets.StockWidget import UIStock


class UISuperMarket(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # setup the mainwindow
        self.setWindowTitle('MASS Supermarket')
        self.setWindowIcon(QIcon('res/images/icon.png'))
        self.centralwidget = QStackedWidget(self)
        self.setCentralWidget(self.centralwidget)
        self.setContentsMargins(0, 23, 0, 0)
        # set exact path to theme files
        self.dark = 'stylesheets/dark.qss'
        self.light = 'stylesheets/light.qss'

        # set current style
        with open('settings.json', 'r') as f:
            settings = json.load(f)
            theme = settings['theme']
            self.applyStyle(theme)

        # setup contents of stacked widget
        self.purchaseWidget = UIPurchase()
        self.productsWidget = UIProducts()
        self.stockWidget = UIStock()
        self.salesWidget = UISales()
        self.centralwidget.addWidget(self.purchaseWidget)
        self.centralwidget.addWidget(self.productsWidget)
        self.centralwidget.addWidget(self.stockWidget)
        self.centralwidget.addWidget(self.salesWidget)

        # set the widget that should be shown at first
        self.setWidget(self.purchaseWidget)
        self.setupMenuBar()
        self.show()

    def setWidget(self, widget):
        """method to set the active widget in the stacked widget"""
        self.centralwidget.setCurrentWidget(widget)

    def applyStyle(self, theme):
        settings = {'theme': theme}
        with open('settings.json', 'w') as f:
            json.dump(settings, f)

        self.style().unpolish(self)
        file = QFile(theme)
        if not file.open(QFile.ReadOnly | QFile.Text):
            raise Exception("FileNotFound")
        style = QTextStream(file)
        self.setStyleSheet(style.readAll())
        self.style().polish(self)
        self.update()

    def setupMenuBar(self):
        """method to setup the menubar"""
        menubar = QMenuBar(self)
        menubar.setGeometry(QRect(0, 0, 5000, 23))
        purchase = menubar.addAction('Purchase')
        products = menubar.addAction('Products')
        stock = menubar.addAction('Stock')
        sales = menubar.addAction('Sales')

        settings = menubar.addMenu('Settings')
        theme = settings.addMenu('Theme')
        light = theme.addAction('light')
        dark = theme.addAction('dark')
        light.triggered.connect(lambda: self.applyStyle(self.light))
        dark.triggered.connect(lambda: self.applyStyle(self.dark))

        purchase.triggered.connect(lambda: self.setWidget(self.purchaseWidget))
        products.triggered.connect(lambda: self.setWidget(self.productsWidget))
        stock.triggered.connect(lambda: self.setWidget(self.stockWidget))
        sales.triggered.connect(lambda: self.setWidget(self.salesWidget))
