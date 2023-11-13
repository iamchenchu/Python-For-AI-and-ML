class Dog :
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        return f"{self.name} barks!"
    
dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Max", "Labrador")

print(dog1.name)   # output is Buddy
print(dog2.name)   # output is Max

class PetDog(Dog):           # class PetDog is getting inherited from the Dog class
    def play(self):
        return f"{self.name} plays fetch!"
    
pet1 = PetDog("Luna", "Poodie")
print(pet1.name)                # output is Luna   even though this attribute is in parent class and this is coz of inheritance
print(pet1.play())              # this is accessing the own method but attribute is from parent class
print(pet1.bark())              # executing the parent method in the child class which is coz of inheritance 