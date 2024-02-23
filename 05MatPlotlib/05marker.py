"""You can use the keyword argument marker to emphasize each point with a specified marker:

marker = """

import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,4,5,7,9])
y = np.array([10, 40, 29, 1, 25])

plt.plot(x, y, marker='D')
plt.show()
