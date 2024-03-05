"""
Methods are functions that belongs to objects

"""
class Student:
    college_name = "University of South Dakota"

    def __init__(self, name, city):
        self.name = name 
        self.from_city = city

    def welcome(self): # class method
        print(f"Hello {self.name}!!, Welcome to {self.college_name} which is in vermillion!!!")

s1 = Student("Urmila", "Jalandhar")
s1.welcome()




    