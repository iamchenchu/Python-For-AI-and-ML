# class Car:
#     color = "Blue"
#     brand = "Mercedes"

# car1 = Car()
# print(car1.brand)
# print(car1.color)

# Constructor 
# All classes will have a function called __init__(), which is always executed when the class is being initiated
# It invokes everytime when I create an object automatically, whether u write the constructor or not 
# it always takes one orgument as an input which is self, which means it indicates to the current object that being used
# self parameter is a reference to the current instance of the class, and is used to access the variables that belongs to the class

class Student:
    name = "Chenchu"
    def __init__(self):
        print(self)
        print("Adding a new student in the database")

s1 = Student() # the parenthsis are is for calling the constructor
print(s1.name)

s2 = Student()
print(s1.name)



    






