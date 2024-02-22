"""
Polymorphism : Operator overloading 
when the same operator is allowed to have different meaning according to the context

"""
# print(3 + 6) # addition 
# print("Chenchu"+ "Reddy") # Concatenation
# print([1, 2, 3]+[6, 5, 9]) # merging 

# All the above above operator overloading happening because someone wrote the code for them and gave us by default with python. So we call all the 
# python default overloading features called implicit overloading 

# Now same thing can happened to the class which is built by the user which is explicit overloading, which we do now 


class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img
    
    def showNumber(self):
        print(self.real,"i",self.img,'j')
    
    def __add__(self, num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal, newImg)
    
    def __sub__(self, num2):
        newReal = self.real - num2.real
        newImg = self.img - num2.img

num1 = Complex(1, 3)
num1.showNumber()
num2 = Complex(4, 6)
num2.showNumber()

num3 = num1 + num2
num3.showNumber()