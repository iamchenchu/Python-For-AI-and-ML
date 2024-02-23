"""To plot only the markers, you can use shortcut string notation parameter 'o', which means 'rings'."""

import matplotlib.pyplot as plt
import numpy as np

x_points = np.array([3, 4, 6, 8, 10])
y_points = np.array([3, 4, 6, 8, 10])

plt.plot(x_points, y_points, 'o')
plt.show()