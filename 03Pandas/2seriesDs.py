#series is a one of the data structures in the pandas 
# series is a one dimentional array either it can be a row or a column 

import pandas as pd                                 # importing the pandas

data = ["Ram","Sita","Krishna","Radha","Ravan"]     # adding the data 

tableform = pd.Series(data)               # the way of creating the series ds
print(tableform)                          # printing the series

print(tableform[2])                      # accessing the elements using series
print(tableform[1:4])                    # accessing the range of elements
print(tableform.iloc[3])                 # accessing the element at position 3
print(tableform.values)                  # printing all the values of seties 
print(tableform.index)                   # RangeIndex(start=0, stop=5, step=1)
print(tableform.shape)                   # prints the dimensions of the series  in this case 5
print(tableform.sum())                   # concatenate the string and print RamSitaKrishnaRadhaRavan
print(tableform.unique())                # prints all the unique values in the series 
print(len(tableform.unique()))           # prints the length of the unique values in the series


