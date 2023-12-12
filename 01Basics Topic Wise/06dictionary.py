# it stores key value pairs and uses {}
# let's create a dict using names and age

dict = {"Rajia":26, "Chenhu":25, "Bujji": 24, "Dad" : 50, "Mom":48, "Pratham":12, "Riya":2, "Jassu": 6}

print(dict) # prints entire dictionary
print(dict.keys()) # prints all the keys of the dict in a list form
print(dict.values()) # prints all the values of the dict in a list form
print("Mom" in dict) # prints True coz "Mom" is present dict
print("riya" in dict) # prints false even though Riya is present in dict coz I wrote the small letter instead of capital 
print(dict["Chenhu"]) # prints 25 which is the value of the key "Chenchu"
dict["Laadi"] = 24 # it will append this to the original dict 
print(dict)
del(dict["Chenhu"]) # it will delete the key and value of "Chenchu"
print(dict)