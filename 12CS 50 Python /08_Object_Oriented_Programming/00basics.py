"""
So far we have seen functional programming, now let's get into the object oriented programming
Up until this point, you have worked procedurally step-by-step.
Object-oriented programming (OOP) is a compelling solution to programming-related problems.
"""

def main():
    name, house = get_student()
    print(f"{name} is from {house}")

def get_student():
    name = input("Name :")
    house = input("House :")
    return name, house

if __name__ == "__main__":
    main()


