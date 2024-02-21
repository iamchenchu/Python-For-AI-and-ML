"""
Constructur : All classes have a function called __init__(), which is always executed when the object is being initiated 
"""
class Student :

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("Adding the new students details to database....")


s1 = Student("Karan", 97)
print(s1.name) # karan

s2 = Student("Arjun", 88)
print(s2.name)