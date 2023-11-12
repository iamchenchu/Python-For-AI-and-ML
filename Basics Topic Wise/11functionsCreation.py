# functions are 2 types which are user defined and in-built functions 
# now we will see an example for user defined example 

def emaiil_Creation():                                     # we use the def keyword to create a function
    fname = str(input("Please enter your first name :"))
    lname = str(input("Please enter your first name :"))
    email = fname+"."+lname+"@usd.com"
    return print("the user email created as : ", email)

emaiil_Creation()
 
def mul(a,b):                                               # a function can have any number of arguments
    c = a*b
    return print(c)                                         # a function must have a return type to return the output of the function 
mul(10,20)

def my_function(*kids):                                     # If the number of arguments is unknown, add a * before the parameter name:
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")
