students = []

with open("students.csv") as file:
    for line in file:
        name, city = line.rstrip().split(",")
        student = {"name":name, "city":city}
        students.append(student)

def get_name(student):
    return student["name"]

for student in sorted(students, key=get_name):
    print(f"{student['name']} is from {student['city']} city.")