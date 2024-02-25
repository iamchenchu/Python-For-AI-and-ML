"""
A lambda fucntion is small anonymous function
A lambda function can take any number of arguments but can have only one expression
"""

x = lambda a : a+10
print(x(10))

c = lambda a, b : a + b
print(c(10, 20))
print(c(20, 5))

def function(n):
    return lambda a : a * n

mydoubler = function(10)
print(mydoubler(2))




