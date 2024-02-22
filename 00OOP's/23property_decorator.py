"""
@property: it is a decorator, we use this on any method in the clas to use the method as a propery 

"""
class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math

    #def calcPercentage(self):
    #    self.percentage = str((self.phy + self.chem + self.math)/3) + "%"

    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math)/3) + "%"

student1 = Student(98, 97, 99)
print(student1.percentage)

student1.phy = 86
print(student1.percentage)