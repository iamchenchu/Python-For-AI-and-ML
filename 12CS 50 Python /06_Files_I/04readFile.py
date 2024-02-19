with open("names1.txt", "r") as file:
    for line in file:
        print("Hello", line.rstrip()) # rstrip() used to remove the extra line space 

