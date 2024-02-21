"""Some operators such as + and - can be “overloaded” such that they can have more abilities beyond simple arithmetic.
In your terminal window, type code vault.py. Then, code as follows:"""

class Vault:

    def __init__(self, galleons=0, sickles=0, knuts=0):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts

    def __str__(self):
        return f"{self.galleons} Gallons, {self.sickles} Sickles, {self.knuts} Knuts"

potter = Vault(100, 50, 25)
print(potter)

weasley = Vault(25, 50, 100)
print(weasley)

galleons = potter.galleons + weasley.galleons
sickles = potter.sickles + weasley.sickles
knuts = potter.knuts + weasley.knuts

total = Vault(galleons, sickles, knuts)
print(total)