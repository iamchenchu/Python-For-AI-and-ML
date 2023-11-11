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

def thesum(*numbers):

    total_sum = sum(numbers)

    return print(total_sum)

thesum((1,2,3,4,5))