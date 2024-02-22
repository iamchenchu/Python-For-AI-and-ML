class Person:
    __name = "Ananymous"

    def __hello(self):
        print("Hello Person")

    def welcome(self):
        self.__hello()
    
p1 = Person()

print(p1.welcome()) # now it's prinitng as we are acessing the method from another public method within the class
print(p1.__hello()) # we can't access the method here as we are calling the private method outside of the class 

