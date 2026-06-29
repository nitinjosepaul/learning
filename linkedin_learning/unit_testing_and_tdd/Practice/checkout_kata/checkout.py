class Checkout:

    class Discount:
        def __init__(self, nbrItems, price):
            self.nbrItems = nbrItems
            self.price = price

    def __init__(self):
        self.prices = {}
        self.discounts = {}
        self.items = {}

    def addItemPrice(self, item, price):
        self.prices[item] = price

    def addItem(self, item):
        if item not in self.prices:
            raise Exception("Item %s is not available" %item)
        else:
            if item in self.items:
                self.items[item] += 1
            else:
                self.items[item] = 1

    def calculateTotal(self):
        total = 0
        for item, count in self.items.items():
            total += self.calculateItemTotal(item, count)
        return total

    def calculateItemTotal(self, item, count):
        total = 0
        if item in self.discounts:
            discount = self.discounts[item]
            if count >= discount.nbrItems:
                total += self.calculateItemDiscountedTotal(item, count, self.discounts[item])

            else:
                total += self.prices[item] * count
        else:
            total += self.prices[item] * count
        return total

    def calculateItemDiscountedTotal(self, item, count, discount):
        total = 0
        nbrOfDiscounts = count // discount.nbrItems
        total += nbrOfDiscounts * discount.price
        remainingItems = count % discount.nbrItems
        total += remainingItems * self.prices[item]
        return total

    def addDiscount(self, item, nbrItems, price):
        discount = self.Discount(nbrItems, price)
        self.discounts[item] = discount