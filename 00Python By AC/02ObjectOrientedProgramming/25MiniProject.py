"""
GUESS THE NUMBER MINI PROJECT

"""

import random 

target = random.randint(1, 100)

while True:
    userChoice = int(input("Please enter a number : "))
    if(userChoice == target):
        print("Wow!! You have guessed the number correctly congratulations!!!!")
        break
    elif(userChoice > target):
        print("Your guess was bigger than the target so guess the smaller value")
        
    else:
        print("Your guess was smaller than the target...guess the bigger value")


print("Game Over")