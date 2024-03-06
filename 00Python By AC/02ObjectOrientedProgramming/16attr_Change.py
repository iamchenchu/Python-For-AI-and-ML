# What if we want to chnage the name or attribute of the class

class Person:
    name = "ananymous"

    def changeName(self, name): # this will work 
        Person.name = name
        # self.__class__ = "Rahul" this will also work
        
p1 = Person()
print(p1.name)
p1.changeName("Chenchu")
print(p1.name)
Person.name = "Bheem" # this will also work
print(p1.name)

    
