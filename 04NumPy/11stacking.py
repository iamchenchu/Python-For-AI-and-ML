"""Finally, stacking is a feature of NumPy that leads to increased customization of arrays. It means to join two or more arrays,
either horizontally or vertically, meaning that it is done along a new axis.

np.vstack() - stacks vertically
np.hstack() - stacks horizontally
np.hsplit() - splits an array into several smaller arrays"""

import numpy as np

a1 = np.array([[1, 2],
               [3, 4]])
a2 = np.array([[5, 6],
               [7, 8]])

print(f"The 1st array is : \n{a1}")
print(f"The 2nd array is : \n{a2}")

# Stack the arrays vertically 
vert_stack = np.vstack((a1, a2))
print(vert_stack)
print(vert_stack.ndim)
print(vert_stack.shape)
print(vert_stack.size)

horiz_stack = np.hstack((a1, a2))
print(horiz_stack)




