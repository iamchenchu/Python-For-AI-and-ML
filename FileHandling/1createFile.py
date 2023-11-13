# You can create a file using open() method in 3 main modes , r, w, a 
# after the creation you can perform your tasks and you will have to make sure that you are closing the file 
# to close the file you can use close() method or you can open the file using with keywork which will close the file automatically 

file = open("file1.txt", "r")  # opened the file in the reading mode
content = file.read()   # reading the file using read() method
print(content)          # printing the all content what ever read() method reads
file.close()            # closing the file after our tasks 



