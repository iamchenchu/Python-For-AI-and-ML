x = int(1)
print(type(x))

y = int(3.9)
print(type(y))

z = int("3")     # we can't cast the other words strings to int
print(type(z))


a = float(1)
b = float("4")
c = float("3.2")
d = float(5.0)
print("these are float values after casting : ", a, b, c, d)
print("there are the types of the converted variables : ", type(a), type(b), type(c), type(d))

a1 = str(1) 
b1 = str(3.2)
c1 = str(3.0)
d1 = str("S1")
print("these are string values after casting : ", a1, b1, c1, d1)
print("These are the types of values of the above variables after casting : ", type(a1), type(b1), type(c1), type(d1))

class1 = ["raam", "bheem", "kiran"]
class2 = set(class1)
print(class2)

class3 = tuple(class2)
print(class3)

class4 = list(class3)
print(class4)

