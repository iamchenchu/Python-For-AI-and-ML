def main ():
    student = get_student()
    if student[0] == "chenchu":
        student[1] = "India"
    print(f"{student[0]} from {student[1]}")



def get_student():
    name = input("Name :")
    house = input("House :")
    return [name, house]                 # If explicityly we want to change the content sometimes then we use the list which is mutable 

def get_student():
    name = input("Name :")
    house = input("House :")
    return (name, house)                 # We are returning the tuple here as we usually don't change the content (tuple is immutable)

if __name__ == "__main__":
    main()
    