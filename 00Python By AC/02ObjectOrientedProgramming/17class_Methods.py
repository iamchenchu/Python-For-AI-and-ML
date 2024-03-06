"""
Clas method : A Class method is bound to the class & receives the class as an implicit first argument
Note : Static method can't access or modify class state & generally for utility

# THERE ARE 3 TYPES OF FUNCTIONS WE USE MAINLY
    1. Static method : we don't use anything as argument
    2. Class Methods : cls as a first argument
    3. Instance mehtods : self as a first argument
"""

class Person:
    name = "anonymous"

    @classmethod
    def changeName(cls, name):
        cls.name = name

p1 = Person()
p1.changeName("Rahul Kumar")
print(p1.name)
print(Person.name)

