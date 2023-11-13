#we can read the files using different methods like read(), readline() and readlines()

file1 = open("file1.txt", "r")
line1 = file1.read()            # read() method reads the entire text file
print(line1)
file1.close()


file2 = open("file2.txt","r")
line2 = file2.readline()          # readline() method reads the 1 line at a time
print(line2)
file2.close()

file3 = open("file3.txt","r")
line3 = file3.readline()          # readline() method reads the 1 line at a time
print(line3)
file3.close()

file4 = open("file4.txt","r")
line4 = file4.readlines()          # readlines() method reads the all lines one by one into a list
print(line4)
file4.close()


