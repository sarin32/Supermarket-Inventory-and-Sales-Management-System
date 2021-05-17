"""
This is the backend of the application
"""
class Cart:
    def __init__(self):
        self.cart = []
        self.total_cost = 0

    def newProduct(self, product_code, units):
        pass

    def purchase(self):
        pass


class Inventory:
    def __init__(self):
        self.brandIds = ['25', '36']
        self.categoryIds = ['36', '45']
        self.productIds = ['65', '36']

    def getAllBrandNames(self):
        return self.brandIds

    def getAllCategoryNames(self):
        return self.categoryIds

    def getAllProductNames(self, brandId=None, categoryId=None):
        return self.productIds

