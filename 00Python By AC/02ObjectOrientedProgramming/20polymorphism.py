"""
Polymorphism : when same operator is allowed to have different meaning according to the context 
Operator overloading
Poly : Many
morphism : Forms
# Getter and Setter
Operators and Dunder Functions: 
a + b            # Addition            a.__add__(b)
a - b            # Subtraction         a.__sub__(b)
a * b            # Multiplication      a.__mul__(b)
a / b            # Division            a.__truediv__(b)
a % b            # mod                 a.__mod__(b)
"""

print(4 + 5) # Addition will happen
print("Chenchu" + "Reddy") # Concatenation will happen
print([1, 2, 3] + [4, 5, 6]) # Merge will happen

# In the above contexts the operator is performing the diffferent tasks depends upon the context 
# This is all implicit overloading which is already coded in the python

# Now we can create our own class and perform 


# Now Let's code the same technique for the complex numbers where we add the complex numbers in the same way as below 
#           3i + 4j
#           4i + 4j
# The Sum : 7i + 8j

