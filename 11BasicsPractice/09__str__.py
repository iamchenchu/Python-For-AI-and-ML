class Person:
    def __init__(self, name, age):
        print("Below are the Persond details :")
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name is : {self.name} and the age is : {self.age}"
p1 = Person("Chenchu", 30)
print(p1)