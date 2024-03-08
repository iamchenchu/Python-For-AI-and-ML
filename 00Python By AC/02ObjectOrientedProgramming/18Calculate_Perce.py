"""
What if we want to calculate the percentage of 3 sub marks and change the marks later after object creation and calculate the average again 
"""

class Student:
    def __init__(self, marks1, marks2, marks3):
        self.sub1 = marks1
        self.sub2 = marks2
        self.sub3 = marks3
        self.percentage = str((self.sub1 + self.sub2 + self.sub3)/3) + "%"

    def calcPercentage(self):
        percentage = str((self.sub1 + self.sub2 + self.sub3)/3) + "%"
        return percentage


student1 = Student(92, 95, 98)
print(student1.percentage)


student1.chemistry = 100 # Changing the object value 
 
print(student1.percentage)   # it's not changing the percentage as it's not getting effected by the object modification
print(student1.chemistry)

print(student1.calcPercentage())



