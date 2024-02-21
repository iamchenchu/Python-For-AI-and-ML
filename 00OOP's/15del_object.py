"""
del keyword : used to delete the object properties or object itself
Example :
del s1.name :  will delete the name attribute in the object s1 in the class
del s1      : will delete the object s1 in the class

"""

class Student :
    def __init__(self, name):
        self.name = name 

    
s1 = Student("Chenchu")
print(s1.name)
# del s1.name
# print(s1.name)
del s1
print(s1)