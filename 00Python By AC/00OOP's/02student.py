def main ():
    student = get_student()
    if student['name'] == 'chenchu':
        student['house'] = 'India'
    print(f"{student['name']} from {student['house']}") # Don't use double quetes within double quetes as it throws an error


def get_student():
    student = {}
    student["name"] = input("Name :")
    student["house"] = input("House :")
    return student                                       # we are returning the dictionaries which are mutable 

if __name__ == "__main__":
    main()