"With Pyplot, you can use the xlabel() and ylabel() functions to set a label for the x- and y-axis."

import matplotlib.pyplot as plt
import numpy as np

year = np.array([2019, 2020, 2021, 2022, 2023])
revenue = np.array([50000, 700000, 1100000, 1550000, 2500000])

plt.plot(year, revenue, marker ='o', ls = 'dashed')
plt.title("Chenchu Revenue From 1st Job")
plt.xlabel("Year")
plt.ylabel("Revenue")

plt.show()