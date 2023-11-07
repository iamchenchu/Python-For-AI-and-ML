

list = ['banana','apple','sapota','pinapple']
print(list)
list[1] ='orange'  # it replace the new value in the place of the old once 
print(list)
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"] 
thislist[1:3] = ["watermilon","orange"]  # it replaces the the values of inxed 1 and 2 with the new list items
print(thislist)
thislist[1:3] = ["mango"] # if we pass only 1 value then it will delete the given number of elemts and replace with the given values
print(thislist)  
thislist.insert(2,"chenchu")  # inset(index, value) it inserts the value at index 2 and adjust the remaining values without deletion
print(thislist)


