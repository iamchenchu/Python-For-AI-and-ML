names = []

for _ in range(4):
    names.append(input("What's your name :"))

for name in sorted(names):
    print(f"hello, {name}")

print(names)


"""After running this program we are able to create the list names and it's giving the output, but when we run the program again
 then we will loose the all previous names from the memory, In such cases the Files Input/Output operations will play the crutial 
role in the scenarios.

open(): is a function, we use this for reading or writing to a file

"""
    
