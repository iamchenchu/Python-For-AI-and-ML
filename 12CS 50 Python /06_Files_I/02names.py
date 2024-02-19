
name = input("what is your name : ")
file = open("names1.txt", "a")
file.write(f"{name}\n") # it saves the name to the file, and go to the next line
file.close()