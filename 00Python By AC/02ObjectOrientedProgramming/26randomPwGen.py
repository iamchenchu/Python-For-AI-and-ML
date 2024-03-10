"""Create a program to generate a random password

using a-z, A-Z, 0-9, [%, /, \,@ ]

"""

import random 
import string

print(string.ascii_letters)
print(string.digits)
print(string.punctuation)

charValues = string.ascii_letters + string.digits + string.punctuation

print(charValues)



password = ""
pw_length = 20

for i in range(pw_length):
    password += random.choice(charValues)

# List comprehensions : [function for i in range(n)]
# password = "".join([random.choice(charValues) for i in range(pw_length)])

print("Your Random password is :",password)