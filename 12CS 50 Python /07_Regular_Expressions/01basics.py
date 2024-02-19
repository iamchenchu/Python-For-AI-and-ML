
# If I want to check my email address being entered is valid or not 

email = input("What is your email address : ").strip()

if "@" in email:
    print("Entered valid email address")
else:
    print("Entered invalid email address")
# it's buggy code as if i entered only @ symbol the would still say as valid so it's not appropriate way 
    

email1 = input("What is your email address : ").strip()

if "@" in email and "." in email1:                 # still it's buggy as if we enter only @ and . it would say valid
    print("Entered valid email address")
else:
    print("Entered invalid email address")