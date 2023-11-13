# to close the file you can use close() method or you can open the file using with keywork which will close the file automatically 


with open("file4.txt", "r") as file1:     # in this we are not closing the file explicitly coz it will be closed automatically
    content = file1.read()
    print(content)


file2 = open("file3.txt","r")            # Here we are using the regular way where we have to close the file explicitly 
line2 = file2.readlines()
print(line2) 
file2.close()
print(file2.name)
print(file2.mode)