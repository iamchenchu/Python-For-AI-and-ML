import numpy as np

arr = np.array([[1, 2, 3],[3, 9, 3]])
print(arr)

one_dimen = np.array([1, 2, 3, 4, 5, 6, 7, 8])

#convert one dimention to multi dimention
multi_dimen = np.reshape(one_dimen,
                         (2,4)) 
print(one_dimen)
print(multi_dimen)

# Finding size, shape and dimension.
print(multi_dimen.ndim)
print(multi_dimen.shape)
print(multi_dimen.size)

"""
[[1 2 3]
 [3 9 3]]
[1 2 3 4 5 6 7 8]
[[1 2 3 4]
 [5 6 7 8]]
2
(2, 4)
8
"""