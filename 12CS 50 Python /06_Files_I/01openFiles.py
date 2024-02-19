
name = input("what's your name : ")

file = open("names.txt", "a")
file.write(name)                  # it won't create name in new lines, instead it it creates names one by one without spaces
file.close()

# Try to run the files from the 06_Files to ignore the file creation out of the directory
# open() : is a function which is used for intialize the name of the file and mode of the file 
# write() : is a function which is used to write names to the file 
# close() : is a function which is used to close the file and save the changes
# "a" : append mode 
# "W" : it created the brand new file everytime we open the file 
# "r" : only reading