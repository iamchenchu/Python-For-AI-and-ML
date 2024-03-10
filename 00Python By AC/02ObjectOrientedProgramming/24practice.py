"""
Let's create a class called Order which stores item and it's prices 

Use Dunder function __gt__() to convey that:

order1 > order2 if price of order1 > price of order 2

"""
class Oder:
    def __init__(self, item, price):
        self.item = item 
        self.price = price

    def __gt__(self, order2):
        return self.price > order2.price 
    

ord1 = Oder("Chips", 20)
ord2 = Oder("Tea", 15)

print(ord1 > ord2) # True
