# we have 2 types of arrays here one is 1D arrays and 2D arrays 
# we use numPy to do lot of scientific calculations

import numpy as np                          # importing the numpy

a = np.array([1,4,2,5,26,76])               # creating the numpy using the np          
print(a)                                    # printing the numpy

print(a[0])                                 # we can access the array using the indexing
print(len(a))                               # we can find the lenght of the array
print(np.__version__)                       # version of the np
print(type(a))                              # prints as numpy.ndarray
print(a.dtype)                              # prints the data type 

