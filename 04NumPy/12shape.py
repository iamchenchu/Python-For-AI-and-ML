# The shape of an array is the number of elements in each dimension.



import numpy as np 

arr = np.array([[1,2,3,4,5],[6,7,8,9,0]])
print(arr.shape)

arr1 = np.array([1, 3, 5, 7, 9], ndmin=5) # creates 5 dimension array
print(arr1)
print("Array dimenstion is :",arr1.ndim)
print("Array shape is :", arr1.shape)
print("Array size is :", arr1.size)

