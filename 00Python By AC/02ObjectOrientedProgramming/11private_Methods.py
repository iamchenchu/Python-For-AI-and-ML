"""
Private(like) attributes and methods : Conceptual implementations in python

Private attributes and methods are meant to be used only within the class and are not accessible from outside the class

"""

class Person:
    __name = "Ram"


    def __hello(self):
        print(f"Hello {self.__name}")

    def welcome(self):
        self.__hello()
        print(f"Welcome to USD MR.{self.__name}")


p1 = Person()
p1.welcome() # this can be accessed and within this welcome function we are also using the private method

#p1.__hello() # We can not call this method outside of the class
