"""
Classes are usually combination of 2 things which are attributes and methods
Methods are functions that are belong to objects

"""

class Student:
    college_name = "University of South Dakota"

    def __init__(self, name, marks):
        self.name = name 
        self.marks = marks

    def welcome(self):

        print(f"{self.name} we are welcoming you to the {self.college_name}")

    def get_marks(self):
        return self.marks
    
s1 = Student("Mekalathuru Chenchaiah", 97)
s1.welcome()
print(s1.get_marks())