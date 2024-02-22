"""
Multiple inheritance : The class is derived from multiple classes at a time 

"""

class A :
    varA = "Welcome to class A"

class B :
    varB = "Welcome to class B"

class C(A, B):  # class c is being derived from multiple classes at a time 
    varC = "Welcome to class C"

c1 = C()
print(c1.varC)
print(c1.varB)
print(c1.varC)



