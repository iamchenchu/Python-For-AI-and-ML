#data frame me is one of the data structures in the pandas
#A DataFrame is a two-dimensional, tabular data structure. it can be thought of as a collection of series, each sharing a common index

import pandas as pd
 
data = {"name":["chenchu","rajia","abhi","laaddi","riya","jassu"],
        "Age":[26,27,24,23,4,6],
        "city":["vermillion","vermillion","chicago","jalandhar","nellore","nellore"]}       # created a data frame using the dictionary

df = pd.DataFrame(data)
print(df)
print(df.columns)       # prints all the names of columns or keys in the list
print(len(df.columns))  # prints the length of the keys
print(df.shape)         # it prints the shape of the matrix size (6,3) means (6 values, 3 keys)
print(df.values)     
 
