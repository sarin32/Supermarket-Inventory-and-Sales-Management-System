from datetime import datetime

from PySide6.QtGui import Qt
from PySide6.QtWidgets import QWidget, QHeaderView, QTableWidgetItem

from SuperMarket import Sales
from ui.sales import Ui_sales
from widgets.UIFunctions import showMessage


class SalesWidget(QWidget, Ui_sales):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.setAttribute(Qt.WA_StyledBackground, True)

        self.sale = Sales()

        self.buttonCheck.clicked.connect(lambda: self.check())
        self.buttonLoad.clicked.connect(lambda: self.setupSalesTableData())

        # setup tables
        header = self.tableSales.horizontalHeader()
        header.setSectionResizeMode(1, QHeaderView.Stretch)
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QHeaderView.ResizeToContents)

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

    def setupSalesTableData(self):
        self.tableSales.setRowCount(0)
        date = self.calendar.selectedDate()
        pydate = str(date.toPython())
        data = self.sale.getSalesDetails(pydate)
        total = self.sale.getTotalSaleAmount()
        if not data:
            showMessage(self, 'Information', 'No sales at specified date')
        for i, row in enumerate(data):
            self.tableSales.insertRow(i)
            for j, item in enumerate(row):
                newItem = QTableWidgetItem(item)
                self.tableSales.setItem(i, j, newItem)
        self.labeldailyAmount.setText(str(total))
