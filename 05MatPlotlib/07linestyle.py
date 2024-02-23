"""
You can use the keyword argument linestyle, or shorter ls, to change the style of the plotted line:

"""
import matplotlib.pyplot as plt 
import numpy as np 

x = np.array([23, 12, 15, 18, 19])
y = np.array([10, 15, 18, 13, 9])

plt.plot(x, y, linestyle = 'dotted')                  # linestyle = 'dashed', dotted can be written as :, linestyle can be written as ls
plt.show()