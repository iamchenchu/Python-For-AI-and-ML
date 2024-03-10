# def : define 
# Creating a function using the def keyword 
# Everythig should be indented within the def code 

def hello(to):
    print(f"Hello {to}")

name = input("enter the name ? ")
hello(name) # function call1 
hello("ram") # function call2
hello(3)
hello([1,2,34])

# We can override the function usind the below format 
# If incase the user forgets to call the function along with the name parameter then we cna use the function override 

def wish(person="world"):
    print(f"Hellow, {person}")

p = input("name of a person :")
wish(p)
wish()  # Function override will work here in this case 



