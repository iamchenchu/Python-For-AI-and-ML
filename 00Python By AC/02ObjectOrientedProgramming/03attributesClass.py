"""
Class.Attribute
obj.Attribute

self.attribute : means this will be different for each object (These are called instance attributes)
Class.Attribute : means the attributes which are same for all the objects then these are called class objects 
"""

class Student:
    college = "University of South Dakota"
    name = "Ananymous"

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("Adding the new student in Database")


s1 = Student("Chenchu", 99)
print(s1.college, s1.name, s1.marks) # object attribute precidence > class attribute presidance if they have same names


