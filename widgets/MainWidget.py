import re

from PySide6.QtCore import QRect, Signal, QObject
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QMainWindow, QStackedWidget, QMenuBar, QDialog

from SuperMarket.users import Users
from ui.addUser import Ui_addUser
from ui.changePassword import Ui_changePassword
from widgets.ProductsWidget import ProductsWidget
from widgets.PurchaseWidget import PurchaseWidget
from widgets.SalesWidget import SalesWidget
from widgets.StockWidget import StockWidget
from widgets.UIFunctions import Theme, showMessage


class Communicate(QObject):
    logout = Signal()


class ChangePasswordDialog(QDialog, Ui_changePassword):
    def __init__(self, parent, user_data):
        QDialog.__init__(self, parent)
        self.user_data = user_data
        self.setupUi(self)
        self.setWindowTitle("Change Password")
        self.buttonCancel.clicked.connect(lambda: self.cancel())
        self.buttonChangePassword.clicked.connect(lambda: self.changePassword())
        self.open()

    def cancel(self):
        self.close()

    def changePassword(self):
        pwd = self.fieldPwd.text()
        cnfrmpwd = self.fieldCnfrmPwd.text()
        pwd_regex = re.compile(r'[A-Za-z0-9@#$%^&+=]{8,20}')

        # validations
        if not 8 <= len(pwd) <= 20:
            showMessage(self, 'Input Error', 'Invalid password. Password should be of length 8 to 20')
            return

        elif not pwd_regex.fullmatch(pwd):
            showMessage(self, 'Input Error',
                        'Invalid password. Password can contain only uppercase and lowercase letters, digits and '
                        'special characters(@,#,$,%,^,&,+,=)')
            return

        elif pwd != cnfrmpwd:
            showMessage(self, 'Input Error', 'Password mismatch')
            return

        else:
            user = Users()
            user.changePassword(self.user_data['username'], pwd)
            showMessage(self, 'Information', 'Password changed successfully')
            self.close()


class AddUserDialog(QDialog, Ui_addUser):
    def __init__(self, parent, user_data):
        QDialog.__init__(self, parent)
        self.user_data = user_data
        self.setupUi(self)
        self.setWindowTitle("Add User")
        self.buttonCancel.clicked.connect(lambda: self.cancel())
        self.buttonAddUser.clicked.connect(lambda: self.addUser())
        self.open()

    def cancel(self):
        self.close()

    def addUser(self):
        username = self.fieldUsername.text()
        pwd = self.fieldPwd.text()
        cnfrmpwd = self.fieldCnfrmPwd.text()

        pwd_regex = re.compile(r'[A-Za-z0-9@#$%^&+=]{8,20}')
        usr_regex = re.compile(r'[A-Za-z0-9_]{5,10}')

        # validations
        user = Users()
        if not 5 <= len(username) <= 10:
            showMessage(self, 'Input Error', 'Invalid username. Username should be of length 5 to 10')
            return

        elif not usr_regex.fullmatch(username):
            showMessage(self, 'Input Error',
                        'Invalid username. Username can contain only uppercase and lowercase letters, digits and '
                        'underscore(_)')
            return

        elif not user.isUsernameAvailable(username):
            showMessage(self, 'Error', 'Username is already taken')
            return

        elif not 8 <= len(pwd) <= 20:
            showMessage(self, 'Input Error', 'Invalid password. Password should be of length 8 to 20')
            return

        elif not pwd_regex.fullmatch(pwd):
            showMessage(self, 'Input Error',
                        'Invalid password. Password can contain only uppercase and lowercase letters, digits and '
                        'special characters(@,#,$,%,^,&,+,=)')
            return

        elif pwd != cnfrmpwd:
            showMessage(self, 'Input Error', 'Password mismatch')
            return

        # if everything fine
        else:
            user.addUser(username, pwd)
            showMessage(self, 'Information', 'New user added successfully')
            self.close()


class MainWidget(QMainWindow):
    def __init__(self, user_data, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user_data = user_data
        # setup the mainwindow
        self.setWindowTitle('MASS Supermarket')
        self.setWindowIcon(QIcon('res/images/icon-128px.png'))
        self.centralwidget = QStackedWidget(self)
        self.setCentralWidget(self.centralwidget)
        self.setContentsMargins(0, 23, 0, 0)
        # set theme name and exact path to theme files in the dictionary
        self.theme = {'dark': 'stylesheets/dark.qss',
                      'light': 'stylesheets/light.qss'}
        thm = Theme(self)
        json_theme = thm.getTheme()
        thm.applyTheme(json_theme)

        # setup contents of stacked widget
        self.purchaseWidget = PurchaseWidget()
        self.productsWidget = ProductsWidget()
        self.stockWidget = StockWidget()
        self.salesWidget = SalesWidget()
        self.centralwidget.addWidget(self.purchaseWidget)
        self.centralwidget.addWidget(self.productsWidget)
        self.centralwidget.addWidget(self.stockWidget)
        self.centralwidget.addWidget(self.salesWidget)

        # set the widget that should be shown at first
        self.setWidget(self.purchaseWidget)
        self.setupMenuBar()

        # custom logout event
        self.communicate = Communicate()

    def setWidget(self, widget):
        """method to set the active widget in the stacked widget"""
        self.centralwidget.setCurrentWidget(widget)

    def setupMenuBar(self):
        """method to setup the menubar"""
        menubar = QMenuBar(self)
        menubar.setGeometry(QRect(0, 0, 5000, 23))

        purchase = menubar.addAction('Purchase')
        purchase.triggered.connect(lambda: self.setWidget(self.purchaseWidget))

        products = menubar.addAction('Products')
        products.triggered.connect(lambda: self.setWidget(self.productsWidget))

        stock = menubar.addAction('Stock')
        stock.triggered.connect(lambda: self.setWidget(self.stockWidget))

        sales = menubar.addAction('Sales')
        sales.triggered.connect(lambda: self.setWidget(self.salesWidget))

        settings = menubar.addMenu('Settings')
        theme = settings.addMenu('Theme')
        light = theme.addAction('light')
        dark = theme.addAction('dark')
        thm = Theme(self)
        light.triggered.connect(lambda: thm.applyTheme('light'))
        dark.triggered.connect(lambda: thm.applyTheme('dark'))

        account = menubar.addMenu('Account')
        logout = account.addAction('logout')
        logout.triggered.connect(lambda: self.logout())
        change_pwd = account.addAction('change password')
        change_pwd.triggered.connect(lambda: self.changePassword())
        if self.user_data['type'] == 'admin':
            add_employee = account.addAction('add employee')
            add_employee.triggered.connect(lambda: self.addEmployee())

    def logout(self):
        # noinspection PyUnresolvedReferences
        self.communicate.logout.emit()

    def changePassword(self):
        ChangePasswordDialog(self, self.user_data)

    def addEmployee(self):
        AddUserDialog(self, self.user_data)
