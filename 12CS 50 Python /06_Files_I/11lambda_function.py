# lambda function : it's a function with no name and anonymous 
# We can use this when don't need to use a function multiple times 
# in this program we will use the lambda function as we only a function to return some value only once 
# lambda function could take any of the variable as aparameter

students = []

with open("students.csv") as file:
    for line in file:
        name, city = line.rstrip().split(",")
        student = {"name":name, "city":city}
        students.append(student)

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['city']} city.")