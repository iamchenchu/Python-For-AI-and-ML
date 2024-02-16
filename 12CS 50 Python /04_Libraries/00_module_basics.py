"""

Consider a module to be the same as a code library.
A file containing a set of functions you want to include in your application.

we use the keyword import keyword to load the module to your computer

"""


import random

coin = random.choice(["heads", "tails"])
print(coin)

# import random : means we are importing everything which is in random, in some cases we may need only specific functons to be used 
# then we use thefrom key word

from random import choice # it imports only choice function, from random module 


is_passed = choice(["YES PASSED", "FAILED"])
print(is_passed)



