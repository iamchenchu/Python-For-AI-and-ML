"""

students = ["Hermione", "Harry", "Ron", "Draco"]
houses = ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherene"]

"""

students = {
    "Hermione": "Gryffindor", 
    "Harry" : "Gryffindor",
    "Ron" : "Gryffindor",
    "Draco": "Slytherin"
}

print(students)

print(students.keys())
print(students.values())

for student in students:  # When we loop the dictionary in pythn, by default it iterates on the keys 
    print(student, students[student], sep=" : ")


