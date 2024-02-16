students = ["Hermione", "Harry", "Ron"]

print(students)
print(students[0])

for i in students:
    print(i)


for s in students:
    print(s)


for i in range(len(students)): # prints 0, 1, 2
    print(i, students[i])


for i in range(len(students)): # 1 Hermione.....
    print(i+1, students[i])



