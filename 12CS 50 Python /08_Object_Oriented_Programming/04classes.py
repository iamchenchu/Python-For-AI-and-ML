class Student:
    def __init__(self, name, home):
        self.name = name
        self.home = home


def main():
    student = get_student()
    print(f"{student.name} is from {student.home}")
    

def get_student():
    name = input("Name : ")
    home = input("Home : ")
    student = Student(name, home)
    return student

if __name__ == "__main__":
    main()
