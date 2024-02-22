"""
When one class (child/derived) derives the properties and methods of another class(parent/base)
there are main 3 types of inheritance 
1. Single Inheritance
2. Multi-level Inheritance
3. Multiple Inheritance

"""
class Car:
    color = "Black"

    @staticmethod
    def start():
        print("Car started...")

    @staticmethod
    def stop():
        print("Car stopped...")

class ToyotaCar(Car):
    def __init__(self, name):
        self.name = name
    
car1 = ToyotaCar("Camry")
car2 = ToyotaCar("Fortunar")

print("The car name is ", car1.name, " and it's color is : ", car1.color) # as we can see here, we are able to access the color of the parent class also from here 
print(car1.start()) # class able to use the parent class method 