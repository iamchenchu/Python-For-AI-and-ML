import matplotlib.pyplot as plt 
import numpy as np

x1 = np.array([12, 16, 18, 20, 27, 14, 18])
y1 = np.array([25, 14, 18, 35, 18, 10, 20])

x2 = np.array([10, 19, 38, 20, 37, 14, 18])
y2 = np.array([15, 10, 12, 25, 28, 20, 16])

plt.title("Random Data")
plt.xlabel("X- Axis")
plt.ylabel("Y- Axis")
plt.plot(x1, y1, x2, y2)
plt.show()

