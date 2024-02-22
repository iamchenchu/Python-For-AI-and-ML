
class Employee:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def showDetails(self):
        print("Role : ", self.role)
        print("Department : ", self.dept)
        print("Salary : ", self.salary)


class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name 
        self.age = age
        super().__init__("Engineer", "IT", "75000")


eng1 = Engineer("ElonMusk", 40)
eng1.showDetails()

