# this program is to save the names to the list of names[] then sort and print the wishing message

names = []

with open("names1.txt") as file:
    for line in file:
        names.append(line.rstrip())  # rstrip() Removes the white spaces and lines

for name in sorted(names):
    print(f"Hello, {name}")
