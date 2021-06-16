import csv

from SuperMarket.brands import Brands
from SuperMarket.categories import Categories


# noinspection PyMethodMayBeStatic
class Products(Brands, Categories):
    def __init__(self):
        self.OUTSTOCK = 'out of stock'
        self.INSTOCK = 'instock'

    def getProductsData(self, p_id=False, name=False, brand=False, category=False, stock=False, prize=False,
                        filterBrand=None, filterCategory=None, filterType=None):
        """:returns a list containing all brand data based on parameters"""
        data = []
        brandId = self.getBrandId(filterBrand)
        categoryId = self.getCategoryId(filterCategory)
        with open('dataFiles/products.txt', 'r') as file:
            reader = csv.reader(file, delimiter='|')
            for row in reader:
                if brandId is not None and brandId != row[2]:
                    continue
                if categoryId is not None and categoryId != row[3]:
                    continue
                if filterType is not None:
                    if filterType == self.INSTOCK and int(row[4]) == 0:
                        continue
                    if filterType == self.OUTSTOCK and int(row[4]) != 0:
                        continue

                subData = []
                if p_id:
                    subData.append(row[0])
                if name:
                    subData.append(row[1])
                if brand:
                    subData.append(self.getBrandName(row[2]))
                if category:
                    subData.append(self.getCategoryName(row[3]))
                if stock:
                    subData.append(row[4])
                if prize:
                    subData.append(row[5])
                data.append(subData)
        if [p_id, name, brand, category, stock, prize].count(True) == 1:
            data = [item for sublist in data for item in sublist]
        return data

    def getProductId(self, product):
        """
        :returns product id of specified brand
        :type product: str
        """
        if product is None:
            return None
        else:
            with open('dataFiles/products.txt', 'r') as file:
                reader = csv.reader(file, delimiter='|')
                for row in reader:
                    if row[1] == product:
                        return row[0]

    def getProductDetails(self, code):
        """
        :type code: str
        """
        details = []
        with open('dataFiles/products.txt', 'r') as file:
            reader = csv.reader(file, delimiter='|')
            for row in reader:
                if code == row[0]:
                    details.append(row[0])
                    details.append(row[1])
                    details.append(self.getBrandName(row[2]))
                    details.append(self.getCategoryName(row[3]))
                    details.append(row[4])
                    details.append(row[5])
                    return details

    def addProduct(self, name, brand, category, stock, prize):
        with open('dataFiles/products.txt', 'r') as file:
            try:
                code = int(file.readlines()[-1].split('|')[0])
            except IndexError:
                code = 0
        with open('dataFiles/products.txt', 'a', newline='') as file:
            writer = csv.writer(file, delimiter='|')
            writer.writerow([code + 1, name, brand, category, stock, prize])

    def deleteProduct(self, p_id):
        lines = []
        with open('dataFiles/products.txt', 'r') as readFile:
            reader = csv.reader(readFile, delimiter='|')
            for row in reader:
                lines.append(row)
                if row[0] == p_id:
                    lines.remove(row)
        with open('dataFiles/products.txt', 'w', newline='') as writeFile:
            writer = csv.writer(writeFile, delimiter='|')
            writer.writerows(lines)

    def isDeletableBrand(self, b_id):
        with open('dataFiles/products.txt', 'r') as readFile:
            reader = csv.reader(readFile, delimiter='|')
            for row in reader:
                if row[2] == b_id:
                    return False
        return True

    def isDeletableCategory(self, c_id):
        with open('dataFiles/products.txt', 'r') as readFile:
            reader = csv.reader(readFile, delimiter='|')
            for row in reader:
                if row[3] == c_id:
                    return False
        return True

    def updateProduct(self, p_id, new_name):
        lines = []
        with open('dataFiles/products.txt', 'r') as readFile:
            reader = csv.reader(readFile, delimiter='|')
            for row in reader:
                lines.append(row)
                if row[0] == p_id:
                    lines[-1][1] = new_name
        with open('dataFiles/products.txt', 'w', newline='') as writeFile:
            writer = csv.writer(writeFile, delimiter='|')
            writer.writerows(lines)

    def updateStock(self, p_id, newStock):
        lines = []
        with open('dataFiles/products.txt', 'r') as readFile:
            reader = csv.reader(readFile, delimiter='|')
            for row in reader:
                lines.append(row)
                if row[0] == p_id:
                    lines[-1][4] = str(int(lines[-1][4]) + int(newStock))
        with open('dataFiles/products.txt', 'w', newline='') as writeFile:
            writer = csv.writer(writeFile, delimiter='|')
            writer.writerows(lines)

    def updatePrize(self, p_id, newPrize):
        lines = []
        with open('dataFiles/products.txt', 'r') as readFile:
            reader = csv.reader(readFile, delimiter='|')
            for row in reader:
                lines.append(row)
                if row[0] == p_id:
                    lines[-1][5] = str(float(newPrize))
        with open('dataFiles/products.txt', 'w', newline='') as writeFile:
            writer = csv.writer(writeFile, delimiter='|')
            writer.writerows(lines)

    def purchase(self,cart):
        lines = []
        with open('dataFiles/products.txt', 'r') as readFile:
            reader = csv.reader(readFile, delimiter='|')
            for row in reader:
                lines.append(row)
                if int(row[0]) in cart.keys():
                    lines[-1][4] = str(int(lines[-1][4]) - int(cart[int(lines[-1][0])]))
        with open('dataFiles/products.txt', 'w', newline='') as writeFile:
            writer = csv.writer(writeFile, delimiter='|')
            writer.writerows(lines)