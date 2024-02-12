# Sequence of data saved in single variable 
# ordered, mutable, duplicates allowed, can save different data types in one variable, type of the class is list
# Also called collection data types in the python programming language List, Tuple, Set, Dictionary


# Creating the list
team = ["ram", "bheem", "suresh", "naresh", "krish", "teja", "ram", "muniram", "vinodh", "subbu"]
print(team)

# Accessing the list
print(team[2]) # 3rd element in the list
print(team[-1]) # last element
print(team[2:]) # all elements after 2nd position 
print(team[3:6])
print(team[-4:-1])

#Addition to list 
team.append("venkat")
print(team)

team.insert(1, "orange")
print(team)

list2 = ["sundhar", "praveen"]

print(list2)
team.extend(list2)
print(team)

#Removing from the list 
team.remove("orange")
print(team)
team.pop(1)
print(team)
team.pop() # removes last item
del team[0]
print(team)
# del team # deletes entire list
# print(team) # will say not defined
#team.clear() # clear all elements and make an empty list 
# print(team)

#Methods
managers = list2.copy()
print(managers)
print(team.count("ram"))
points = [1, 4, 2, 9, 7, 8, 9, 3, 1]
print(points.count(9))
print(points.index(3))
team.sort()
print(team)
print(len(team))
list1 = ["a", "b", "c"]
list3 = [1, 2, 3]

list4 = list1 + list3
print(list4)






