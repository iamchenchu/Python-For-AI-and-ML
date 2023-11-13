# We can write to files without losing any of the existing data as follows by setting the mode argument to append: a. 
#you can append a new line as follows:

with open("/Users/mekalathuruchenchaiah/Desktop/PROGRAMMING/Python For AI and ML/FileHandling/example.txt","a+") as file1:
    appendline1 = file1.write("this si the line 4\n")
    appendline2 = file1.write("this si the line 5\n")

    file1.seek(0)
    content = file1.read()
    print(content)
