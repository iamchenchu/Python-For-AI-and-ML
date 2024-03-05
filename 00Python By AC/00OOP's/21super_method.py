"""
super() function  : in Python is used to give access to methods and properties of a parent or sibling class. It returns a temporary object 
of the superclass that allows you to call its methods or access its properties. This is particularly useful in inheritance, especially 
when you want to extend or modify the functionality of inherited methods.

"""
class Car:
    def __init__(self, type):
        self.type = type

    @staticmethod
    def start():
        print("Car started...")

    @staticmethod
    def stop():
        print("Car stopped...")

class ToyotaCar(Car):
    def __init__(self, name, type):
        super().__init__(type)
        self.name = name
        super().start()

car1 = ToyotaCar("Prius", "electric")
print(car1.type)