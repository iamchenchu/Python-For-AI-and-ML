# sets are also a type of collection
# just like in tuples and lists you can input any type for sets
# uses {} for creation 
# we can not access the set using slicing 

A = {3,4,5,6,7,9,0}                      # a set A
B = {1,2,3,4,5,6,7}                      # set B
C = [1,4,3,6]                            # list
print(C)                                 # prints the list 
print(set(C))                            # type casting  of list
print(A)                                 # prints entire set A but in random order as this does not follw the ordering 
print(B)                                 # prints entire set B but in random order as this does not follw the ordering 
A.add(11)                                # adding an element to the set using the add()
print(A)
A.remove(4)                              # removing an element using remove()
print(A)
print(9 in A )                           # prints True coz 9 is present in the set A
D = A & B                                # will create a set of D with common elements in A and B
print(D)                                 # prints the entire D set
print(D.issubset(A))                     # prints True coz D is a subset of A


 


