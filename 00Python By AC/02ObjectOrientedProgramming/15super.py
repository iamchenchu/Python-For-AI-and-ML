"""
Super :  super() method is used to acees the methods of the parent class

"""

class Car:
    def __init__(self, type):
        self.type = type 

    @staticmethod
    def start():
        print("The car started...")

    @staticmethod
    def stop():
        print("The card stopped....")
        
class ToyotaCar(Car):
    def __init__(self, name, type):
        super().__init__(type)
        self.name = name


car1 = ToyotaCar("Prius", "electric")
print(car1.type) # can access as we are doign this usign the super method 
print(car1.name)
