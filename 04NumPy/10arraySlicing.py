import numpy as np

two_dim_array = np.array([[1, 2, 3],
                          [4, 5, 6],
                          [7, 8, 9]])

# Select element number 8 from the 2D array using i, j
print(two_dim_array[2][1])
print(two_dim_array[0][0])
print(two_dim_array[0:2]) # prints all the rwos from start to end-1
print("prints 1st row and 1st colums :",two_dim_array[:,1]) # prints 1st column
print(" Prints the 2md colums : ",two_dim_array[:,2]) # Prints the 2md colums
print(two_dim_array[:, 0]) # Prints the 0th colums

