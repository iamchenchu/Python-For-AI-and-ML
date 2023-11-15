# more operations 

import pandas as pd
import matplotlib.pyplot as plt

dict_ = {'a':[11,21,31],'b':[12,22,32]}    # created a dictionary
df = pd.DataFrame(dict_)                   # DataFrame is multi dimentional DataStructure 

print(df)                                   # printing the entire dataFrame
print(df.mean())                            # mean or the average will be printed here 
print(df.head())                            # When you call the method head the dataframe communicates with the API displaying the first few rows of the dataframe.


# now this modules are a simple API's which work offline within our system, we use REST api's for communicating through the internet 

#output
"""    a   b
0  11  12
1  21  22
2  31  32
a    21.0
b    22.0
dtype: float64
    a   b
0  11  12
1  21  22
2  31  32
"""