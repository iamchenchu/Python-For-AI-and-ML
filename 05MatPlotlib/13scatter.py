"""The scatter() function plots one dot for each observation. It needs two arrays of the same length, one for the values of the x-axis,
and one for values on the y-axis:
"""
import numpy as np 
import matplotlib.pyplot as plt 

x = np.array([5, 7, 32, 52, 37, 28, 16, 25,28, 19])
y = x.copy()-5

plt.scatter(x, y, marker='o', color = 'r')
plt.title("Scatter Example")
plt.xlabel("X-Axis")
plt.ylabel("Y-Label")
plt.show()
