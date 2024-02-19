
students = []

with open("students.csv") as file:
    for line in file:
        name, city = line.rstrip().split(",")
        student = {"name":name, "city":city}
        students.append(student)

for student in students:
    print(f"{student['name']} is from {student['city']} city.")


