import csv
from datetime import datetime


# noinspection PyMethodMayBeStatic
class Sales:
    def __init__(self):
        self.total_amount = 0

    def getSalesDetails(self, date):
        date = datetime.strptime(date, '%Y-%m-%d')
        date = datetime.strftime(date, '%d/%m/%Y')
        self.total_amount = 0
        with open('dataFiles/sales.txt', 'r') as readFile:
            data = []
            reader = csv.reader(readFile, delimiter='|')
            for row in reader:
                if row[1] == date:
                    data.append(row)
                    self.total_amount += float(row[3])
        return data

    def getMonthlySaleAmount(self, month, year):
        with open('dataFiles/sales.txt', 'r') as readFile:
            amt = 0
            reader = csv.reader(readFile, delimiter='|')
            for row in reader:
                date = datetime.strptime(row[1], '%d/%m/%Y')
                if date.month == month and date.year == year:
                    amt += float(row[3])
        return amt

    def getTotalSaleAmount(self):
        return self.total_amount

    def newSale(self, amount):
        with open('dataFiles/sales.txt', 'r') as file:
            try:
                sales_id = int(file.readlines()[-1].split('|')[0])
            except IndexError:
                sales_id = 0
        with open('dataFiles/sales.txt', 'a', newline='') as file:
            writer = csv.writer(file, delimiter='|')
            data = [str(sales_id + 1), str(datetime.now().strftime('%d/%m/%Y')),
                    str(datetime.now().strftime("%I:%M %p")), str(amount)]
            writer.writerow(data)