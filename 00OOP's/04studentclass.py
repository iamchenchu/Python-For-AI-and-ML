class Student:
    def __init__(self, name, house):    #Initializing the attributes of the class it is also called as dundur method or magic method
        self.name = name
        self.house = house

def main ():
    student = get_student()
    print(f"{student.name} from {student.house}")       


def get_student():
    name = input("Name :")
    house = input("House :")
    student = Student(name, house)
    return student                                       

if __name__ == "__main__":
    main()