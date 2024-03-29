import numpy as np

greet = "Good morning!!"
print(greet)

# Create Array using numpy
a = np.array([1,2,3])
print(a)

#Creating the array with integers from 0 to till the range we give
array = np.arange(5)
print(array)

#Create an array that starts from integer 1  and ends at 20 and increased by 3
c = np.arange(1, 20, 3)
print(c)

#Create an array from the start to end with the number of equal divisions
linespaced_arr = np.linspace(0, 200, 10) # will be devided into 10 equal units 
print(linespaced_arr)

# We can also make this as an integer array 
linespaced_array = np.linspace(0, 200, 10, dtype=int)
print(linespaced_array)

# we can also create an array which will range from start till end with the certain gap in between
arr1 = np.arange(0, 30, 3)
print(arr1)

# We can also make this as float 
arr2 = np.arange(0, 30, 3, dtype=float)
print(arr2)

arr3 = np.arange(30, dtype=float) # prints from 0 to till 30
print(arr3)


char_arr = np.array(["Welcome to the Data Science!!"])
print(char_arr)
print(char_arr.dtype)

"""
Good morning!!
[1 2 3]
[0 1 2 3 4]
[ 1  4  7 10 13 16 19]
[  0.          22.22222222  44.44444444  66.66666667  88.88888889
 111.11111111 133.33333333 155.55555556 177.77777778 200.        ]
[  0  22  44  66  88 111 133 155 177 200]
[ 0  3  6  9 12 15 18 21 24 27]
[ 0.  3.  6.  9. 12. 15. 18. 21. 24. 27.]
[ 0.  1.  2.  3.  4.  5.  6.  7.  8.  9. 10. 11. 12. 13. 14. 15. 16. 17.
 18. 19. 20. 21. 22. 23. 24. 25. 26. 27. 28. 29.]
['Welcome to the Data Science!!']
<U29

"""