"""
A class method is bound to the class and receives the class as an implicit first argument

Note : Static method can't access or modify class state and generally for utility

there are multiple ways to do that 

"""


class Person:
    name = "anonymous"

    # def changename(self, name):
    #     self.__class__.name = "Rahul"
    
    @classmethod
    def changeName(cls, name):
        cls.name = name

p1 = Person()
p1.changeName("Rahul Kumar")
print(p1.name)
print(Person.name)