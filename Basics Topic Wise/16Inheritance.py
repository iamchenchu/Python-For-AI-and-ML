#Inheritance allows us to define a class that inherits all the methods and properties from another class.
#Parent class is the class being inherited from, also called base class. Child class is the class that inherits from another class, also called derived class.

class Person :                                 # this is a base class and parent class
    def __init__(self, fname,lname):
        self.fname = fname
        self.lname = lname
    def printName(self):
        print(self.fname, self.lname)

p1 = Person("Chenchu", "Reddy")
p1.printName()

class Student(Person):
    pass                                     # we can write pass keyword here if we don't have any attributes or methods to define 

x = Student("Mike","Olsen")
x.printName()                                 # we did not initialize any methods or attributes in the child class but still it is taking the help from parent and executing the code

# When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.
#By using the super() function, you do not have to use the name of the parent element, it will automatically inherit the methods and properties from its parent.

class Employee(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)

e = Employee("Rajia", "Rani")
e.printName()

    