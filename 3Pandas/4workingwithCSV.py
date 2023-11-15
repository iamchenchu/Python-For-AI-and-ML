

import pandas as pd

data = pd.read_csv("mock_data.csv")

print(data)
print(data.shape)     # prints the shape of the data in this case (1000 values, 6 keys)
print(data.keys)      # prints all the keys
print(data.values) 
print(data["first_name"])     # prints all the values of first name
print(data["last_name"])      # prints all the values of last name
new_data = data["first_name","last_name"]
new_data.to_csv("exportfile.csv", index = False)

