with open("students.csv") as file:
    for line in file:
        row = line.rstrip().split(",")
        print(f"{row[0]} is from {row[1]}")

"""
name, city = line.rstrip().split(",")
print(f"{name} is from {city}")""" # this also work 