"""
del keyword : used to delete object properties or object


"""

class Student:
    def __init__(self, name, marks):
        self.name = name 
        self.marks = marks

s1 = Student("Chenchu", 99)

print(s1.name)
print(s1.marks)

del s1.name
print(s1.name) # Gives error as I deleted the name property
del s1
print(s1) # gives error as I deleted the entire object 