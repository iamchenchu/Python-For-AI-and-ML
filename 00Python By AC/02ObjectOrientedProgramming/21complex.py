# Now Let's code the same technique for the complex numbers where we add the complex numbers in the same way as below 
#           3i + 4j
#           4i + 4j
# The Sum : 7i + 8j

class Complex :
    def __init__(self, real, img):
        self.real = real
        self.img = img 
    
    def showNumber(self):
        print(self.real, "i +", self.img,'j')


num1 = Complex(1, 3)
num1.showNumber()
num2 = Complex(4, 5)
num2.showNumber()