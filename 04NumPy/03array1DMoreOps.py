
import numpy as np

a = np.array([0,1,2,3,4,5,6,78,9,10])   
print(a)

print(a.size)                     # prints the size of the array
print(a.sum())                    # prints the sum of the all elements
print(a.max())                    # prints the max of the all elements
print(a.mean())                   # prints the mean of all the elements
print(a.shape)                    # The attribute shape is a tuple of integers indicating the size of the array in each dimension
print(a.min())                    # prints the min value in the elements
print(a.ndim)                     # prints the number of the array dimentions or rank of the array
print(a.std())                    # prints the standard deviation of the array

"""
[ 0  1  2  3  4  5  6 78  9 10]
10
118
78
11.8
(10,)
0
1
22.279138223908035

"""