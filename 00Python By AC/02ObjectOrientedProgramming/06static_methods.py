"""
Methods that don't use the self parameter (works at class level)
We don't use the self parameters in the static methods 
Decorators : Decorators allow us to wrap another function in order to extend the behaviour of the wrapped function, without permanently modyfying it

"""
class Student:
    city = "Vermillion"
    def __init__(self, name):
        self.name = name
        #self.city = city

    #@staticmethod
    def hello():
        print("Hello to the world of decorators!!")

    def welcome(self):
        print(f"Hi {self.name}, Welcome to the {self.city} city.")
        self.hello()

s1 = Student("Chenchu Reddy")
s1.welcome()
s1.hello()
