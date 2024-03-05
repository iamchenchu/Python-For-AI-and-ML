"""
Creata a student class that takes name and marks of 3 subjects as arguments in constructor. the create a method to print the average

"""
class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    

    def average(self):

        for v in self.marks:
            sum = 0
            sum += v
        print(f"The student {self.name} got the average score of {sum/3}")
    
        

s1 = Student("Chenchu", [80, 93, 95])
s1.average()
