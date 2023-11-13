# It's a concept of restricting acess to certain parts of an object to prevent unintended modification
# In python we can use private and protected access modifiers to achieve the same 
# unlike in other languages we use underscores here to specify the access modifiers 
# self.name  (Public member)  self._project (Protected member which is accessable within the calss and it's subclasses)  self.__salary (Private member which is accessable within the class)

class Cat :
    def __init__(self, name, breed):
        self._name = name                          # single underscore so protected attribute
        self.__breed = breed                       # double underscore so it is a private attribute
    def meow(self):
        return f"{self.name}  meows all the time!!" 
cat1 = Cat("Whiskers", "Siamese")
print(cat1._name)   # Accessing the protected is allowed 
#print(cat1.__breed)  # this will give an error 





