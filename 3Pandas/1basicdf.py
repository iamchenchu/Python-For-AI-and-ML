#data frame me is one of the data structures in the pandas
#A DataFrame is a two-dimensional, tabular data structure. it can be thought of as a collection of series, each sharing a common index

import pandas as pd
 
data = {"name":["chenchu","rajia","abhi","laaddi"],"Age":[26,27,24,23]}   # created a data frame using the dictionary

df = pd.DataFrame(data)

print(df)

