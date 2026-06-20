class InvalidProductIndexError(Exception):
    pass

class OutOfStockError(Exception):
    pass

class InvalidQuantityError(Exception):
    pass

class EmptyInventoryError(Exception):
    pass


class Inventory:
    def __init__(self, products):
        self.products = products

    def purchase(self, index, quantity):
        if len(self.products) == 0:
            raise EmptyInventoryError("EmptyInventoryError")

        if index < 0 or index >= len(self.products):
            raise InvalidProductIndexError("InvalidProductIndexError")

        if quantity <= 0:
            raise InvalidQuantityError("InvalidQuantityError")

        if quantity > self.products[index]:
            raise OutOfStockError("OutOfStockError")

        self.products[index] -= quantity
        print(self.products[index])


# Input
n = int(input())

products = []
if n > 0:
    products = list(map(int, input().split()))

index = int(input())
quantity = int(input())

inventory = Inventory(products)

try:
    inventory.purchase(index, quantity)
except Exception as e:
    print(e)