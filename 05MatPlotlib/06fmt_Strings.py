"""You can also use the shortcut string notation parameter to specify the marker.
This parameter is also called fmt, and is written with this syntax:
marker|line|color
# _ -> solidline, : -> dotted line, __ -> dashed line, -. -> Dashed/dotted line
# 'r' : red, 'g' : green, 'b' : blue, 'c' : cyan, 'm' : magenta, 'y' : yellow, 'k' : black, 'w' : white

"""

import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,4,5,7,9])
y = np.array([10, 40, 29, 1, 25])

plt.plot(x, y, 'o:r')   
plt.show()