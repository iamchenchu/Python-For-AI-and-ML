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


s1 = Student(99, 95, 98)
print(s1.percentage)
print(s1.calcPercentage())

s1.sub3 = 85
print(s1.percentage)  # will show the wrong value 
print(s1.calcPercentage())  # will work



