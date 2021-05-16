import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QApplication, QMenuBar, QMainWindow, QStackedWidget, QWidget

from purchase import Ui_purchase


class UISuperMarket(QMainWindow):
    def __init__(self):
        super().__init__()

        # self.resize(800, 600)
        self.setWindowTitle('MASS Supermarket')
        self.setWindowIcon(QIcon('res/images/icon.png'))
        self.centralWidget = QStackedWidget(self)

        purchase = QWidget()
        ui = Ui_purchase()
        ui.setupUi(purchase)
        self.centralWidget.addWidget(purchase)
        self.centralWidget.setCurrentWidget(purchase)

        self.setupMenuBar()
        self.show()

    def setupMenuBar(self):
        menubar = QMenuBar(self)
        menubar.setGeometry(QRect(0, 0, 5000, 20))
        purchase = menubar.addMenu('Purchase')
        newProduct = menubar.addMenu('New Product')
        updateStock = menubar.addMenu('Update Stock')
        ViewStock = menubar.addMenu('Stock')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = UISuperMarket()
    sys.exit(app.exec_())
