class Student:
    ...                           #pass


""" Now we have a special data type called Student which data attributes or instance variables could be mutable and 
    immudtable and we need to write some extra code for that """

def main ():
    student = get_student()
    print(f"{student.name} from {student.house}")        # Don't use double quetes within double quetes as it throws an error


def get_student():
    student = Student()
    student.name= input("Name :")
    student.house = input("House :")
    return student                                        # we are returning the dictionaries which are mutable 

if __name__ == "__main__":
    main()