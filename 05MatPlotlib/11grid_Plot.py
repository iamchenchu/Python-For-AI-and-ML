import matplotlib.pyplot as plt 
import numpy as np 

x = np.array([10, 20, 30, 40, 50, 65, 75])
y = x.copy()-5

plt.plot(x, y, marker = 'o', color = 'r', linestyle = 'dotted')

plt.title("Random Data Points")
plt.xlabel("X - Label")
plt.ylabel("Y - Label")
plt.grid()

plt.show()




