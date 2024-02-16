"""
EXCEPTION HANDLING:

Try     : The try block lets you test a block of code for errors.
Except  : The except block lets you handle the error.
Else    : The else block lets you execute code when there is no error.
Finally : The finally block lets you execute code, regardless of the result of the try- and except blocks.

"""
try:
    x = int(input("what is x : "))
except ValueError:
    print("x is not an integer")
else:
    print(f"x is {x}")

    