"""
EXCEPTION HANDLING:

Try     : The try block lets you test a block of code for errors.
Except  : The except block lets you handle the error.
Else    : The else block lets you execute code when there is no error.
Finally : The finally block lets you execute code, regardless of the result of the try- and except blocks.

"""

def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
            try:
             return int(input("what is x :"))
            except:
                pass     # it does not exit the loop it will keep ignoring the state of the statement, so it will keep on running until currect answer
    
main()