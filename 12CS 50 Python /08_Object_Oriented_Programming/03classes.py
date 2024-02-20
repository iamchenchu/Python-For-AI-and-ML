"""
Classes are the blue prints of the objects 
it will let us create our own type of the datatypes and give them a name

__init__(): instance method or thunder method 
"""

class Student:
    pass

def main():
    student = get_student()
    print(f"{student.name} is from {student.home}")
    print(type(student))

def get_student():
    student = Student()
    student.name = input("Name :")
    student.home = input("Home :")
    return student

if __name__ == "__main__":
    main()