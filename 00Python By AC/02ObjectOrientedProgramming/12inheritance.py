"""
Inheritance : When one class (child/derived) derives the properties & methods of another class(parent/base)

"""

class Car:

    @staticmethod
    def start():
        print("Car Started...")

    @staticmethod
    def stop():
        print("Car Stopped...")
    
class ToyotaCar(Car):
    def __init__(self, name):
        self.name = name

car1 = ToyotaCar("Fortunar")
car2 = ToyotaCar("Prius")

car1.start()
print(car1.name)
car2.stop()
print(car2.name)
