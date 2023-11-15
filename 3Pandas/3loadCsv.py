# we can load all most all any table format data to the pandas
# here let's see how can we load the .csv data to the pandas
# we use the read_csv() method to load the csv data to the pandas

import pandas as pd

data = pd.read_csv("mock_data.csv")                    # loading the data to python using the read_csv() methos

print(data)                                            # printing the data of csv file

