"""
This is the backend of the application
updates the file system as well as retrieves the content from the file system
"""
import csv


class Cart:
    def __init__(self):
        self.cart = []
        self.total_cost = 0
        self.inv = Inventory()

    def newProduct(self, product_code, units):
        self.cart.append([product_code, units])

    def getTotalCost(self):
        return self.total_cost

    def isExistingProduct(self, code):
        for item in self.cart:
            if code == item[0]:
                return True
        return False

    def getCartTable(self):
        data = []
        self.total_cost = 0
        for item in self.cart:
            details = self.inv.getProductDetails(str(item[0]))
            details[4] = str(item[1])
            details.append(str(item[1] * float(details[5])))
            self.total_cost += float(details[6])
            data.append(details)
        return data

    def removeProduct(self, code):
        for item in self.cart:
            if item[0] == code:
                self.cart.remove(item)
                return

    def getCartItemsCode(self):
        codes = []
        for item in self.cart:
            codes.append(item[0])
        return codes

    def makePurchase(self):
        lines = []
        with open('dataFiles/products.txt', 'r') as readFile:
            reader = csv.reader(readFile, delimiter='|')
            for row in reader:
                lines.append(row)
                if int(row[0]) in self.getCartItemsCode():
                    lines[-1][4] = str(int(lines[-1][4]) - int(self.getUnit(int(lines[-1][0]))))
        with open('dataFiles/products.txt', 'w', newline='') as writeFile:
            writer = csv.writer(writeFile, delimiter='|')
            writer.writerows(lines)
        # TODO: add purchase data in file

    def getUnit(self, code):
        for item in self.cart:
            if item[0] == code:
                return item[1]

    def clearCart(self):
        self.cart.clear()
# noinspection PyMethodMayBeStatic
class Inventory:
    def __init__(self):
        self.OUTSTOCK = 'out of stock'
        self.INSTOCK = 'instock'

    def getBrandsData(self, b_id=False, name=False):
        """:returns a list containing all brand data based on parameters"""
        data = []
        with open('dataFiles/brands.txt', 'r') as file:
            reader = csv.reader(file, delimiter='|')
            for row in reader:
                subData = []
                if b_id:
                    subData.append(row[0])
                if name:
                    subData.append(row[1])
                data.append(subData)
        if [b_id, name].count(True) == 1:
            data = [item for sublist in data for item in sublist]
        return data

    def getCategoriesData(self, c_id=False, name=False):
        """:returns a list containing all brand data based on parameters"""
        data = []
        with open('dataFiles/categories.txt', 'r') as file:
            reader = csv.reader(file, delimiter='|')
            for row in reader:
                subData = []
                if c_id:
                    subData.append(row[0])
                if name:
                    subData.append(row[1])
                data.append(subData)
        if [c_id, name].count(True) == 1:
            data = [item for sublist in data for item in sublist]
        return data

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

    def getBrandId(self, brand):
        """
        :returns brand id of specified brand
        :type brand: str
        """
        if brand is None:
            return None
        else:
            with open('dataFiles/brands.txt', 'r') as file:
                reader = csv.reader(file, delimiter='|')
                for row in reader:
                    if row[1] == brand:
                        return row[0]

    def getCategoryId(self, category):
        """
        :returns category id of specified category
        :type category: str
        """
        if category is None:
            return None
        else:
            with open('dataFiles/categories.txt', 'r') as file:
                reader = csv.reader(file, delimiter='|')
                for row in reader:
                    if row[1] == category:
                        return row[0]

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

    def getBrandName(self, brandId):
        """
        :returns brand name of specified brand
        :type brandId: str
        """
        if brandId is None:
            return None
        else:
            with open('dataFiles/brands.txt', 'r') as file:
                reader = csv.reader(file, delimiter='|')
                for row in reader:
                    if row[0] == brandId:
                        return row[1]

    def getCategoryName(self, catId):
        if catId is None:
            return None
        else:
            with open('dataFiles/categories.txt', 'r') as file:
                reader = csv.reader(file, delimiter='|')
                for row in reader:
                    if row[0] == catId:
                        return row[1]

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

    def addBrand(self, brand):
        with open('dataFiles/brands.txt', 'r') as file:
            try:
                code = int(file.readlines()[-1].split('|')[0])
            except IndexError:
                code = 0
        with open('dataFiles/brands.txt', 'a', newline='') as file:
            writer = csv.writer(file, delimiter='|')
            writer.writerow([code + 1, brand])

    def addCategory(self, category):
        with open('dataFiles/categories.txt', 'r') as file:
            try:
                code = int(file.readlines()[-1].split('|')[0])
            except IndexError:
                code = 0
        with open('dataFiles/categories.txt', 'a', newline='') as file:
            writer = csv.writer(file, delimiter='|')
            writer.writerow([code + 1, category])

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

    def deleteBrand(self, b_id):
        lines = []
        with open('dataFiles/brands.txt', 'r') as readFile:
            reader = csv.reader(readFile, delimiter='|')
            for row in reader:
                lines.append(row)
                if row[0] == b_id:
                    lines.remove(row)
        with open('dataFiles/brands.txt', 'w', newline='') as writeFile:
            writer = csv.writer(writeFile, delimiter='|')
            writer.writerows(lines)

    def isDeletableCategory(self, c_id):
        with open('dataFiles/products.txt', 'r') as readFile:
            reader = csv.reader(readFile, delimiter='|')
            for row in reader:
                if row[3] == c_id:
                    return False
        return True

    def deleteCategory(self, c_id):
        lines = []
        with open('dataFiles/categories.txt', 'r') as readFile:
            reader = csv.reader(readFile, delimiter='|')
            for row in reader:
                lines.append(row)
                if row[0] == c_id:
                    lines.remove(row)
        with open('dataFiles/categories.txt', 'w', newline='') as writeFile:
            writer = csv.writer(writeFile, delimiter='|')
            writer.writerows(lines)

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

    def updateBrand(self, b_id, new_name):
        lines = []
        with open('dataFiles/brands.txt', 'r') as readFile:
            reader = csv.reader(readFile, delimiter='|')
            for row in reader:
                lines.append(row)
                if row[0] == b_id:
                    lines[-1][1] = new_name
        with open('dataFiles/brands.txt', 'w', newline='') as writeFile:
            writer = csv.writer(writeFile, delimiter='|')
            writer.writerows(lines)

    def updateCategory(self, c_id, new_name):
        lines = []
        with open('dataFiles/categories.txt', 'r') as readFile:
            reader = csv.reader(readFile, delimiter='|')
            for row in reader:
                lines.append(row)
                if row[0] == c_id:
                    lines[-1][1] = new_name
        with open('dataFiles/categories.txt', 'w', newline='') as writeFile:
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
