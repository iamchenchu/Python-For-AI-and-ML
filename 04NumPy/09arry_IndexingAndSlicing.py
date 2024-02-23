import numpy as np

array = np.array([1, 2, 4, 6, 9, 11, 45, 16, 13, 92])
print(array[6])
print(len(array))
print(array[-1])
print(array[:1])
print(array[1:9])
# Slice the array a to get the array [2,3,4]
print(array[1:4])
# Slice the array a to get the array [1,2,3]
print(array[ :3])
# Slice the array a to get the array [8,9,10]
print(array[7:])


a = ([1, 2, 3, 4, 5])
print(a[:])
print(a[::])
print(a)
print(a == a[:] == a[::])

"""
45
10
92
[1]
[ 2  4  6  9 11 45 16 13]
[2 4 6]
[1 2 4]
[16 13 92]
[1, 2, 3, 4, 5]
[1, 2, 3, 4, 5]
[1, 2, 3, 4, 5]
True

"""

