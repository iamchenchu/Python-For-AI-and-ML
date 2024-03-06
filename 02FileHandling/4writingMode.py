# "w" specifies that intend to write data to the file
# We use the with statement to ensure that the file is automatically closed when the code block exits. This helps manage resources efficiently.
# in this example I want to write to the file and also I want to read it so I will open it in the "w+" mode for reading and writing

with open("writing.txt","w+") as file1:   # opens the file in writing mode, it creates the new file if the file doesnot exist in the dir
    file1.write("this is line A \n")     # this line will be written to the file 
    file1.write("this is line B \n")      # this line will be written to the file 
    file1.write("this is line C \n")  
    # Reset the file pointer to the beginning to read the content
    file1.seek(0)
    content = file1.read()               # this read() method will read the all the content in the file and store it in the content variable
    print(content)                       # prints the content 




with open("example.txt", "w+") as file:
    # Write to the file
    file.write("Hello, world!\n")
    file.write("This is a second line.\n")

    # Reset the file pointer to the beginning to read the content
    file.seek(0)

    # Read the entire content
    content = file.read()
    print("Content:")
    print(content)