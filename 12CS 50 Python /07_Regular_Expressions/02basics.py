# Let's try to make it more affective 

email = input("What's you email : ").strip()

username, domain = email.split("@") # it returns the 2 words of list 
if username and "." in domain:      # this statement contains 2 boolean expressions, first one is it should contain some string or char to be true 
    print("Valid")
else:
    print("Invalid")

# this code seems bit ok but still it's buggyy for certain situations 

email1 = input("What's your email : ").strip()

username1, domain1 = email1.split("@")
if username and domain1.endswith(".edu"):
    print("Valid")
else:
    print("Invalid")

