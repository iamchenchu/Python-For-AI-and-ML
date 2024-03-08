"""
Define a Circle class to create a circle with radius r using the constructor.
Define an Area method of the class which calculates the area of the circle.
Define a Perimeter method of the class which allows you to calculate the perimeter of the circle.
"""
class Circle:

    pi = 22/7

    def __init__(self, r):
        self.radious = r

    def area(self):
        return (self.pi * self.radious * self.radious)
    
    def perimeter(self):
        return (2 * self.pi * self.radious)
    

circle1 = Circle(10)
print(circle1.area())
print(circle1.perimeter())

    