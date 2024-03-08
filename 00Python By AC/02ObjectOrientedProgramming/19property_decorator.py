"""
Property Decorator : We use @property decorator on any method in the class to use the method as a property

"""

class Student:
    def __init__(self, phy, chem, math):
        self.physics = phy
        self.chemistry = chem
        self.maths = math
        self.percentage = str((self.physics + self.chemistry + self.maths)/3) + "%"


student1 = Student(92, 95, 98)
print(student1.percentage)


student1.chemistry = 100 # Changing the object value 
 
print(student1.percentage)   # it's not changing the percentage as it's not getting effected by the object modification