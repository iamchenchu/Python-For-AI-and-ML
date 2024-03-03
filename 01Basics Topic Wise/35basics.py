# multiple assignment 
a, b, c = 10, 20, 30
print(a, b, c)
fruits = ["Apple", "Banana", "Cherry"]
c, d, f = fruits

print(c, d, f)

x = "python"
y = "is"
z = "awesome"

print(x, y, z) # printing multiple variables at a time in single function 
print(x + y + z) # concatenation
print(" ".join([y, x, z])) # joinging the iterables
print("{} {} {}".format(x, y, z)) # formating string
print(f"{x} {y} {z}") # f string
print(f"%s %s %s" %(x, y, z)) # old method using % operator
