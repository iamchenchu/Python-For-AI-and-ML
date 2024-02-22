class Oder:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, ord2):
        return self.price > ord2.price
    
order1 = Oder("Chips", 40)
order2 = Oder("Tea", 20)

print(order1 > order2)

# operator overloading