"""
Let's Practice
Create student class that takes name & marks of 3 subjects as arguments in constructor.
Then create a method to print the average

"""

class Student:
    college_name = "University of south Dakota"
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        # self.marks2 = marks2
        # self.marks3 = marks3

    def average(self):
        average = int((self.marks[0]+self.marks[1]+self.marks[2])/3)
        print(f"The student got the average marks of {average} from {self.college_name}")

student1 = Student("Mekalathuru Chenchaiah",[94, 96, 99])
student1.average()

