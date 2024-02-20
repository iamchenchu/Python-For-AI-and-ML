def main():
    student = get_student()
    if student['name'] == "Rajia":
        student["home"] = "Jalandhar"
    print(f"{student['name']} from {student['home']}")

def get_student():
    student = {
        "name":input("Name : "),
        "home":input("Home : ")
    }
    return student

if __name__ == "__main__":
    main()

