import random

class Hat:

    houses = ["Gryffindor", "Hufflepuf", "Revenclaw", "Slytherin"]

    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))

Hat.sort("Harry")

"""Notice how the __init__ method is removed because we don’t need to instantiate a hat anywhere in our code. self, therefore, is no longer 
relevant and is removed. We specify this sort as a @classmethod, replacing self with cls. Finally, notice how Hat is capitalized by 
convention near the end of this code, because this is the name of our class."""