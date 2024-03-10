name = input("Please enter the name :")

# Removes the white spaces from the string 
name = name.strip()

# Capitalize the name first letter 
name = name.capitalize()

# Capitalize the first letter in the each word
name = name.title()

# Say hello to the user
print(f"hello, {name}")

student = input("Please enter student name : ").strip().title()
print(f"Hello {student}, Please learn python properly")

# Take full name as an input and split them into first and last names and say hello with the first name 
fullname = input("Please enter your full name : ").strip().title()

first_nanme, last_name = fullname.split(" ")

print(f"Your First name is :{first_nanme} and your last name is : {last_name}")

