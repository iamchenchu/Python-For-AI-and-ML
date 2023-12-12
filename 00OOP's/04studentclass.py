class Student:
    def __init__(self, name, house):    #Initializing the attributes of the object the class it is also called as dundur method or magic method
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

"""Object Creation:

When you create a new instance of a class, Python automatically calls the __new__ method to create the object.
After the object is created, the __init__ method is called to initialize the object's attributes.
"""

def main ():
    student = get_student()
    print(student)      


def get_student():
    name = input("Name :")
    house = input("House :")
    student = Student(name, house)
    return student                                       

if __name__ == "__main__":
    main()