"""Arithmetic operators
Assignment operators
Comparison operators
Logical operators
Identity operators
Membership operators
Bitwise operators"""

# "Arithmetic operators  : +, -, *, /, %, //, **"
a = 10 # we are using the assignment operator here 
b = 3
print("Value of a+b is :", a+b)
print("Value of a-b is :", a-b)
print("Value of a*b is :", a*b)
print("Value of a/b is :", a/b)
print("Value of a%b is :", a%b)
print("Value of a//b is :", a//b)
print("Value of a**b is :", a**b)

# Assignment operators : =, +=, -=, *=, /=, %=, //=, &=, |, ^=, >>=, <<=
a += b
print("Value of a+=10 is :",a)
a -= b
print("Value of a+=b is :", a)
a *= b
print("Value of a*=b is :", a)

c = 10
d = 5
# Comparison operators : ==, !=, >, <, >=, <=
print(c==d)
print(c!=d)
print(c>d)
print(c<d)
print(c>=d)
print(c<=d)

# Logical Operators : and, or, not 
print(c!=d and c > d)
print(c!=d or d > c)
print( not c > d)

# Identity operators : is, is not
e = 10
f = 10

print(f is e) # returns True if both variables have the same object
print(d is not f)   # returns True if both variables don't have the same object

# Membership operators : in, not in

team = ['a', 'b', 'c', 'd', 'f', 'g']
print('a' in team) #Returns True if a sequence with the specified value is present in the object
print('z' not in team) 

#Bitwise operators : &(AND) , |(OR), ^(XOR), ~(NOT), <<, >>
print(6 & 3) 
print(6 | 3)
print(6 ^ 3) 
print(~3)











