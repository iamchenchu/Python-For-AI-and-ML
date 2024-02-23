import numpy as np 

arr1 = np.array([1, 2, 3, 4, 5, 7])

arr2 = arr1.copy() # it does not affect the parent at any cost as it become separe variable now 

print(arr2.shape)
print(arr2.ndim)

arr3 = arr1.view() # affects the parent if u change anything the child tooo
print(arr3)
arr3[2] = 100
print(arr1)


