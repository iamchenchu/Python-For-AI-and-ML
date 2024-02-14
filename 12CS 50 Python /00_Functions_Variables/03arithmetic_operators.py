# Arithmetic Operators : +, -, *, /, %
# In python by default the input will be treated as a string, if you want to specify the input type then you have to make sure to do typecasting 

x = int(input("What is x :"))
y = int(input("what is y :"))

z = x + y
print(f"The sum of the {x} and {y} is {z}")

z1 = x - y
print(f"The subtraction of the {x} and {y} is {z1}")

z2 = x * y
print(f"The multiplication of the {x} and {y} is {z2}")

z3 = x / y
print(f"The division of the {x} and {y} is {z3}")

a = float(input("what is a ?"))
b = float(input("what is b ?"))

c = round(a + b)

print(c)


# Printing the lot of decimal points and limiting them as per our requirements
a1 = float(input("what is the a1 ? "))
b1 = float(input("what is the b1 ?"))

c1 = a1/b1
d1 = a1/b1

print(c1) # prints all the decimal points
print(f"{d1:.2f}") # prints only 2 decimal points
print(f"{d1:.3f}") # prints 3 deicmal points 
