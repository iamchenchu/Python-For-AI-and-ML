with open("names1.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    print("Hello,",line)  # this prints the Hello, name but it also leaves 1 whole line of space in between, to prevent this we use rstrip() method