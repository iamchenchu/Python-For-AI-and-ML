import numpy as np

# One of the advantages of using NumPy is that you can easily create arrays with built-in functions such as:

# np.ones() - Returns a new array setting values to one.
arr = np.ones(5)
print(arr)
# np.zeros() - Returns a new array setting values to zero.
arr2 =np.zeros(10)
print(arr2)
# np.empty() - Returns a new uninitialized array.
arr3 = np.empty(10)
print(arr3)
# np.random.rand() - Returns a new array with values chosen at random
arr4 = np.random.rand(5)
print(arr4)

"""
[1. 1. 1. 1. 1.]
[0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
[0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
[0.92167487 0.96508652 0.71081889 0.21615101 0.44925937]
"""