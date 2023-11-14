# we can import some data using .csv into this program 
# we can take all the necessary data applying the methods or attributes 
# we can also copy the data to new .csv file here and create the new one with the new name 

import pandas as pd

df = pd.read_csv("organizations-10000.csv")                                 # read .csv
print(df)
print(df.head)                                                              # first 5 rows will be printed 
unique_years = df["Founded"].unique()
print(len(unique_years))
orgs_After2000 = df[df["Founded"] > 2000]
print(orgs_After2000)
orgs_After2000.to_csv("orgs_After2000.csv",index=False)                     # exporitng to .csv 
print(len(orgs_After2000))
print(df.describe())                                                        # it Generates summary statistics for numerical columns.