"""
Static methods : Methods those don't use self parameters(works at class level)
@staticmethod # using this @ decorator we are defining the static method

Decorators : allow us to wrap another function in order to extend the behaviour of the wrapped function, without permanently modyfying it

"""
class Student:
    college = "University of South Dakota"
    def __init__(self, name, marks):
        self.name = name 
        self.marks = marks


    @staticmethod  # Decorator 
    def hello():
        print("Hello!!!")
    
    def get_avg(self):
        sum=0
        for val in self.marks:
            sum += val
        
        print(f"Hi {self.name} you got aveage score of {sum/len(self.marks)} from {self.college}")

student1 = Student("Mekalathuru Chenchaiah", [98, 94, 95, 96])
student1.get_avg()
Student.hello() # or student1.hello()   # it's kind of attribute which is global to the class, which can be accesed though the the Class as well as object 
