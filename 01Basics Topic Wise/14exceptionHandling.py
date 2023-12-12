# we use exception handling  to handle the errors during the execution 
# we usually use try, except, else , finally keywords to handle these errors in different way

try:                                          # we can write anything here, if an error occurs here then we print except part
    print(x)
except:                                       # this block will get executed when ever error occurs in the try block
    print("An exception occured")


try:
    print(y)
except NameError:                             # if you want to create many except blocks for different errors, you can do that 
    print("name 'y' is not defined")
except :
    print("Something else went wrong")        # if any error other than the Nameerror this block will be printed

try:
    a = int(input("please enter the a value :"))
    b = int(input("please enter the b value :"))
    c = a*b
    print(c)
except NameError:
    print("variable  is not defined")
except :
    print("something went wrong")
else : 
    print("seems everything excuted well")       # if there are no errors then this will excuted 

finally :
    print("I will get excuted everytime irrespective of error raises or not")  # The finally block, if specified, will be executed regardless if the try block raises an error or not.