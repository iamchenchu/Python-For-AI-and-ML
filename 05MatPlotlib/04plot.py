"""If we do not specify the points on the x-axis, they will get the default values 0, 1, 2, 3 etc., depending on the length of the y-points.
So, if we take the same example as above, and leave out the x-points, the diagram will look like this:"""

import matplotlib.pyplot as plt 
import numpy as np

x = np.array([4, 2, 7, 19])

plt.plot(x)
plt.show()

