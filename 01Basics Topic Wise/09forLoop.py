# if we wanted to do a task multiple times under some conditions then we may use the topic called loops
# we use range() function in this loops
# we can also use the loops for iterating the lists and tuples

lists = [3,2,4,1,5,7,2,7,10,11]
print(range(len(lists))) # prints range(0,10) coz we have 11 elements here

for list in range(len(lists)):     # here we are iterating the list using the for loop by using the range function
    print(lists[list])
print("The task is over")


# we can also print the tables using the loop 

number = 10
for i in range(number):
    print("10 * ", i+1 ," = ",(i+1)*number)  # here we can not use the + symbol to concatenate the string and output 







