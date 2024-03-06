"""
Abstraction :  Hiding the implementation of a class and only showing the essential features to user

Encapulation : Wrapping data and functions into a single unit (Object) : means what ever we did so far, we are creating functions and attributed and wrapping them into objects 
"""
class Car :
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self):
        self.clutch = True
        self.acc = True
        print("The car started..") # Now this will print only the print statemement but will not show unnecessary steps which means abstraction

    
car1 = Car()
car1.start() 
