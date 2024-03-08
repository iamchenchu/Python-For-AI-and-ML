"""
Define a Employee class with atttributes role, department and salary. this class also has the showdetails method

Create Engineer class that inherits the properties from the employee and 

"""

class Employee:
    def __init__(self,role, department, salary):
        self.role = role
        self.department = department
        self.salary = salary
    
    def showDetails(self):
        print("Role : ",self.role)
        print("Department :", self.department)
        print("Salary : ", self.salary)

    
e1 = Employee("Accountant", "Finance", 40000)
e1.showDetails()

class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__("Engineer", "IT", "75000")

engineer1 = Engineer("Chenchu", "27")

engineer1.showDetails()

