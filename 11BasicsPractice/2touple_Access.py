

touple = ("chenchu","reddy","oragne","banana","ram","bhim")
print(touple[1]) # prints the index 1 element 
print(touple[1:3]) #prints the elemets from 1st index till the 2nd won't include the 3rd element 
print(touple[-1]) # prints the last element
print(touple[:4]) # prints all the elements till the 3rd 

for x in touple :   # accessing the elemts using the for loop is also possible 
    print(x)

print(touple[2:]) # it prints all the elemts from the 2nd index

if "reddy" in touple :
    print("Yes reddy is present in the touple")
else :
    print("the word is not present in the touple")
