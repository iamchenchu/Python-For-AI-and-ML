import numpy as np

array_1 = np.array([2, 3, 4, 5, 6, 7])
array_2 = np.array([1, 2, 3, 4, 6, 6])

#Adding the 1D arrays
addition = array_1 + array_2 
print(addition)

#Subtracting the 1D arrays
substraction = array_1 - array_2
print(substraction)

#Multiplication
multiplication = array_1 * array_2
print(multiplication)

# Division
div1 = array_1/2
print(div1)

# Scalar Multiplication
s_multiplication = array_1 * 1.6
print(s_multiplication)


"""
[ 3  5  7  9 12 13]
[1 1 1 1 0 1]
[ 2  6 12 20 36 42]
[1.  1.5 2.  2.5 3.  3.5]
[ 3.2  4.8  6.4  8.   9.6 11.2]
"""

