
import numpy as np

a = np.array([32,12,54,76,23,54,23,64,98,18,25])      # created the 1D array

print(a)

a[0] = 100                  # assigning the new value to the array 
print(a)                    # array being printed using the new assigned value 
print(type(a))              # the type of the array will be printed as ndarray
print(a[1:6])               # prints all the elements from 1st to till 5
print(a[1:5:2])             # prints the elements from 1 to 4th with 2 as range as gap 
print(a[:4])                # prints all the elements till 3 index means 4 elements
print(a[4:])                # prints all the elements form the 4th element
print(a[1:5:])              # even though we don't mention the range it consider the default as 1 and prints from 1st index to till 4th
print(a[1:8:2])             # prints all the even index elements



list =np.array([1,2,6,4,7,98,14])     # creation of new list
print(list)                         # printing the list
indexlist = [0,1,3,4]               # 
c = list[indexlist]                    # passing select list as an index of list
print(c)

