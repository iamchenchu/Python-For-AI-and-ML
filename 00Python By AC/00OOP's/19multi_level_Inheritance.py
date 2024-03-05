"""
Multi-level Inheritance : It can derive the child class from one class which parent to the current class but parent also would have another parent
from which it's being derived

"""
class Car:
    @staticmethod
    def start():
        print("Car started....")

    @staticmethod
    def stop():
        print("Car stopped....")

class ToyotaCar(Car):
    brand = "Toyota"
    

class Fortunar(ToyotaCar):            # multi level inheritance here -> Fortunar is getting derived from ToyotaCar and ToyotaCar is derived from Car class, 
    def __init__(self, type):         # now object in fortunar class can access the attributes and methods in Car class and Toyota class
        self.type = type  

car1 = Fortunar("Electric")    
print(car1.brand)
car1.start()
car1.stop()


