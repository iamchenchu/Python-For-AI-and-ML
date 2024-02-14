"""
print(*objects, sep='', end='\n', file = sys.stdout, flush=False)

we can override the print function and change the default behaviour
"""

print("chenchu")
print("reddy")

print("ram", end=" ") # we changed the \n to simple space
print("Bheem")

name = input("Enter the name : ")
print("Krisha",name, sep="???")


# Format string or fstring 
print(f"the name is {name}")
