"""
There are 4 main pillars in the Object orieneted programming 
1. Abstraction 
2. Encapsulation
3. Inheritance
4. Polymorphism 

Abstraction : Hiding the implementation details of a class and showing the essential features to the end user
Encapsulation : Wrapping the data and functions into a single unit(Object)
"""

class Car:
    def __init__(self):
        self.accelrator = False
        self.brk = False
        self.clutch = False

    def start(self):
        self.clutch = True
        self.accelrator = True
        print("The car is started....")
    
car1 = Car()
car1.start()

# Now here in this case we have created the function start() in a class and performing the actions and printing only necessary 
# info which is called Abstraction 


