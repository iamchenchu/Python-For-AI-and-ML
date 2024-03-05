class Circle:

    def __init__(self, radious):
        self.radious = radious

    def area(self):
        return (22/7) * self.radious ** 2
    
    def perimeter(self):
        return 2 * 3.14 * self.radious
    
c1 = Circle(21)
print(c1.area())
print(c1.perimeter())
