"""
You can plot as many points as you like, just make sure you have the same number of points in both axis.
"""

import matplotlib.pyplot as plt
import numpy as np 

xpoints = np.array([1, 2, 3, 4, 5])
ypoints = np.array([2, 8, 2, 0, 10])

plt.plot(xpoints, ypoints)
plt.show()