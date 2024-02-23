import numpy as np
import matplotlib.pyplot as plt 

# Plot1
x = np.array([0, 1, 3, 5, 4, 9])
y = x.copy()*3

plt.subplot(2, 1, 1) # 2 rows 1 colum and 1st plot
plt.plot(x,y)


# Plot2
x1 = np.array([4, 6, 8, 9, 13, 19])
y1 = x1.copy() * 2
plt.subplot(2, 1, 2) # 2 rows 1 column 2nd plot
plt.plot(x1, y1)

plt.title("SubPlots")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")

plt.show()
