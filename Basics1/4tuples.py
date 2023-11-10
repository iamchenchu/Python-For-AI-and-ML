
t = (1,"chenchu",4, True,"Rajia","Ram", "Bhim") # tuple can be formed using any type of data type 
print(t) # returns the tuple 
print(t[0]) # returns the first element
print(t[-1]) # returns the last element 
print(t[0:3]) # returns the element of 0,1,2 indexes
# tuple is immutable so we can not modify the original tuple but we can create the new tuple using the original tuple 

t2 = t + (4,5,6)
print(t2)  # prints the entire new tuple this time 
print(len(t2)) # prints the length of 10
print(type(t2)) # prints the type as tuple
t3 = (3,5,7,3,63,5,2)
t4 = sorted(t3)
print(t4) # prints the sorted tuple 
print(t[1][2]) # prints e, it acces the index of my 1 index





