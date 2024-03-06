# Multiple Inheritance : the child class will inherit from 2 parent classes at a time

class A:
    varA = "Welcome to class A"
class B:
    varB = "Welcome to class B"
class C(A, B):
    varC = "Welcome to class C"
c1 = C()

print(c1.varA)
print(c1.varB)
print(c1.varC)


