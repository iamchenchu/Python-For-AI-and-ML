"""
Single Inheritance : will get inherited from single parent class
Multi Level Inheritance : the class is derived from a class which is inherited from another class
Multiple Inheritance : the child class will inherit from 2 parent classes at a time

"""

# Multi Level Inheritance
class Car:
    @staticmethod
    def start():
        print("Car started....")

    @staticmethod
    def stop():
        print("Car stopped....")

class ToyotaCar(Car):
    def __init__(self, brand):
        self.brand = brand

class Fortuner(ToyotaCar):
    def __init__(self, type):
        self.type = type

    
car1 = Fortuner("Diesel")
car1.start()


