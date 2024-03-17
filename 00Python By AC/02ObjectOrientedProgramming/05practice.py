"""
Creata a student class that takes name and marks of 3 subjects as arguments in constructor. the create a method to print the average
"""
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average(self):
        for v in self.marks:
            sum = 0
            sum += v
        print(f"Hi {self.name}, you got the average score of {sum/3} in your last semester.")
    
        

s1 = Student("Chenchu", [80, 93, 95])
s1.average()

s1.name = "Rajia" # now the name of the object s1 will be changed
s1.average()


