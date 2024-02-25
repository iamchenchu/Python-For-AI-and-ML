"""
Object's also contains methods, methods in objects are functions that belong to the object
"""

class Person :
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def myfun(self):
        print("Hello my name is :", self.name)
        print("My age is : ",self.age)
        print("I am from : ", self.city)

p1 = Person("Chenchu", 30, "Tirupati")
p1.myfun()