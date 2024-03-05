"""
Class and Instance Attributes : the variables in the class are called attributes 
Let's assume an example that you are soting all the data from your university, in this case univ name is same for everyone so we will not declare this 
within the constructor instead we will store this in the class which is known as class attribute

"""

class Student:
    college_name = "University of South Dakota"
    name = "anonymous"  # Class Attribute

    def __init__(self, name, marks):
        self.name = name # Object Attributes and object attributes will have more precidence as compare to class if bothe have the same names
        self.marks = marks 
        print("Adding the students details to the university database... ")

s1 = Student("Chenchaiah Mekalathuru", 92)
print(f"{s1.name} scored {s1.marks} from {Student.college_name}")

