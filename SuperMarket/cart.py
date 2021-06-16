from SuperMarket.products import Products
from SuperMarket.sales import Sales


class Cart(Products, Sales):
    def __init__(self):
        super().__init__()
        self.cart = {}
        self.total_cost = 0

    def newProduct(self, product_code, units):
        self.cart[product_code] = units

    def getTotalCost(self):
        return self.total_cost

    def isExistingProduct(self, code):
        if code in self.cart.keys():
            return True

    def getCartTable(self):
        data = []
        self.total_cost = 0
        for k, v in self.cart.items():
            details = self.getProductDetails(str(k))
            details[4] = str(v)
            details.append(str(v * float(details[5])))
            self.total_cost += float(details[6])
            data.append(details)
        return data

    def removeProduct(self, code):
        del self.cart[code]

    def makePurchase(self):
        self.purchase(self.cart)
        self.newSale(self.total_cost)

    def clearCart(self):
        self.cart.clear()
