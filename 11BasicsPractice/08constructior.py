"""
To understand the meaning of classes we have to understand the built-in __init__() function.
All classes will have a function called __init(), which is always executed when the class is being initiated.
use the __init__ function to assign values to object properties, or other operations that are necessary to do when object is being created:
"""

class Person:
    def __init__(self, name, age):
        print("These are the Person details")
        self.name = name
        self.age = age
        


p1 = Person("Chenchu", 30)
print(p1.name)
print(p1.age)

print(p1)
