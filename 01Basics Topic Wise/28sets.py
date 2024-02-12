# Sets are used to store multiple items in a single variable.
# set is unordered, unchangeable*, unindexed
# Set items are unchangeable, but you can remove items and add new items.
# Sets are written with curly brackets.

fruits = {"apple", "sapota", "cherry", "orange", "kiwi","sapota", True, 1, 2}
print(type(fruits))
print(fruits) # Note: Sets are unordered, so you cannot be sure in which order the items will appear.
print(fruits) # Duplications not allowed, it prints only one time for every duplicate 

# Note: The values True and 1 are considered the same value in sets, and are treated as duplicates:
# Note: The values False and 0 are considered the same value in sets, and are treated as duplicates:

set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

set1.add("lemon")
print(set1)

set1.update(set2) # adds elements of set2 to set1
print(set1)

list1 = [1, 3, 5, 9]

set2.update(list1)
print(set2)

set2.remove(5)
print(set2)












