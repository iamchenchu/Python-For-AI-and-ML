#Python is an object oriented programming language.
#Almost everything in Python is an object, with its properties and methods. A Class is like an object constructor, or a "blueprint" for creating objects.
#The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.

class Person :
    def __init__(self,name,age,city,language): 
        self.name = name
        self.age = age
        self.city = city
        self.language = language

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, City: {self.city}, Language: {self.language}"

p1 = Person("Chenchu",25,"Tirupati","Telugu")

print(p1)    # you can access each attribute of the object p1 by calling p1.name or p1.age but
             #to print all the attributes at time weneed to use __str__() method to convert all the object attributes to strings



"""def display(self):
        print("Name is : "+ self.name)
        print("Age is : "+str(self.age))
        print("The city is : "+ self.city)
        print("The language is : "+ self.language)"""


#The string representation of an object WITHOUT the __str__() function:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1)

#The string representation of an object WITH the __str__() function:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("John", 36)

print(p1)