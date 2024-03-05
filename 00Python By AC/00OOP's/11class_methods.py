"""
Create a class and instantiate object with subject marks as inputs and print average

"""

class Student:
    college = "University of South Dakota"

    def __init__(self, name , marks):
        self.name = name
        self.marks = marks
    

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print(f"Hi {self.name}, you got the average score of : {sum/len(self.marks)} from {Student.college}")

student1 = Student("Mekalathuru Chenchaiah", (92, 97, 99, 93))
student1.get_avg()
