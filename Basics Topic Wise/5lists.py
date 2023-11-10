# the main difference between the tuple and list is that the list is mutable and tuple is not 

l = [1,"chenchu",4, True,"Rajia","Ram", "Bhim"]
print(l) # returns the tuple 
print(l[0]) # returns the first element
print(l[-1]) # returns the last element 
print(l[0:3]) # returns the element of 0,1,2 indexes
l2 = l + [4,5,6]
print(l2)  # prints the entire new tuple this time 
print(len(l2)) # prints the length of 10
print(type(l2)) # prints the type as tuple
l3 = [3,5,7,3,63,5,2]
l4 = sorted(l3)
print(l4) # prints the sorted tuple 
print(l[1][2]) # prints e, it acces the index of my 1 index

# tuple is immutable so we can not modify the original tuple but we can create the new tuple using the original tuple
# list is mutable so we can modify the list as per our requirement

l.append("ramarao")
print(l)
l.extend([1,3,2])
print(l)
l.append([1,3,2]) # adds as nested list
print(l)
print(len(l)) # prints the length of l
print(l[len(l)-1][0]) # accessing the last element first index
