name = "Chenchu Reddy" # name is a variable which stores the value of string which is Chenchu Reddy

print(name[0]) # prints the first index of the string
print(len(name)) # prints the length of the string
print(name[-1]) # prints the last letter of the string
print(name[12]) 
c = name[::3] # stores every 3rd index of the string name in c 
print(c)
print(name[:6]) # prints all the first 6 letters fron the string 
print(name[1:6]) # prints the all letters from index 1 to till 5
print(name.upper()) # prints entire string in uppercase
print(name.lower()) # prints entire string in lowercase
d =name[0:10:2]# d stores every 2nd index of the string name from 1st index till the 9th index
print(d)
print(name+" he is the best") # concatinating the string 
print(3*name) # prints the name 3 times
name = name + name
print(name) # we can not mutate the string but can create new string 
print(" Michael Jackson \n is the best" )  # \n is the new line in a string 
print(" Michael Jackson \\ is the best" ) # if u want to use the \ within the statement then u should use \\ (2 backslaces)
wife = name.replace('Chenchu','Rajia')
print(wife) # can create new string 