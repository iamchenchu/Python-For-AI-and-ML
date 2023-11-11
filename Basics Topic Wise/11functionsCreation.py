# functions are 2 types which are user defined and in-built functions 
# now we will see an example for user defined example 

def emaiil_Creation():
    fname = str(input("Please enter your first name :"))
    lname = str(input("Please enter your first name :"))
    email = fname+"."+lname+"@usd.com"
    return print("the user email created as : ", email)

emaiil_Creation()

def mul(a,b):
    c = a*b
    return print(c)
mul(10,20)