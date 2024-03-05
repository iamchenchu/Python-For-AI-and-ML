class Student:
    # Default constructor, if we don't create this, python will create this automaticaly
    def __init__(self):
        pass

    # Parameterized constructoe
    def __init__(self, name, marks, city):
        self.name = name
        self.marks = marks
        self.city = city
        print("Adding the new student in the database...")

s1 = Student("Chenchu", 97, "Vermillion")
s2 = Student("Praveen", 99, "Vermillion")
s3 = Student("Triveni", 100, "Vermillion")

print(s1.name, s1.marks, s1.city)
print(s2.name, s2.marks, s2.city)
print(s3.name, s3.marks, s3.city)