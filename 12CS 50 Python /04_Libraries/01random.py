import random

number = random.randint(1, 10)  # generates a random number between 1 to 10 random.randin
print(number)

cards = ["jack", "queen", "kind"]
random.shuffle(cards)    # shuffles the cards in the list
for card in cards:
    print(card)



