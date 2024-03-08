"""
Property Decorator : We use @property decorator on any method in the class to use the method as a property

"""

class Student:
    def __init__(self, phy, chem, math):
        self.physics = phy
        self.chemistry = chem
        self.maths = math
        self.percentage = str((self.physics + self.chemistry + self.maths)/3) + "%"
    @property
    def calPercentage(self):
        return str((self.physics + self.chemistry + self.maths)/ 3) + "%"
    

s1 = Student(99, 98, 97)

print(s1.calPercentage) # now we can call this as an attribute we no need to call this as a methods 

s1.physics = 63 # changes the marks 

print(s1.calPercentage) # automatically it changes after changign the object attribute value also 

    
 