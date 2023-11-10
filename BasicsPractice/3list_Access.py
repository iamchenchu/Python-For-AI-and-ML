

list =['chenchu',1,2,3,True,False,'Reddy']
print(list[1])
print(list[0])     # now we are acessing the list using the index of the element
print(list[-1])  # -1 represents the last element in the list and we can access the list in the reverse order in this way

for x in list :   # we can traverse the list using the for loop  here 
    print(x)

print(list[2:5])  # starts print from index 2 to till 4 (won't include the 5)
print(list[:4])  # it peints the values till 3rd element (prints 4 values from 0 index) 
print(list[2:]) # it start prints all the elements from the index 2 which means it will leave the 2 values and start print all the remaining 
print(list[-4:-1]) # it starts prints from the 4th element from the last till 1st element till the 2nd element from the last, won't include the 1st one from the last

