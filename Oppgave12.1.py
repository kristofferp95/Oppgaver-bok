from Kap12GeometricObject import GeometricObject
import math

class Triangle(GeometricObject):
    def __init__(self, side1 = 0, side2 = 0, side3 = 0):
        super().__init__()

        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def getSide1(self):
        return self.side1
    
    def getSide2(self):
        return self.side2
    
    def getSide3(self):
        return self.side3
    
    def getArea(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        a = math.sqrt(s*(s-self.side1)*(s-self.side2)*(s-self.side3))
        return a
    
    def getPerimeter(self):
        perimeter = self.side1 + self.side2 + self.side3
        return perimeter
    
    def __str__(self):
        return f'Triangle: side1 = {self.side1}, side2 = {self.side2}, side3 = {self.side3}'

def main():
    side1 = float(input(f'Enter side1: '))
    side2 = float(input(f'Enter side2: '))
    side3 = float(input(f'Enter side3: '))
    color = input(f'Enter color: ')
    filled = input(f'Enter 1/0 for filled (1: True, 0: false): ')

    triangle = Triangle(side1, side2, side3)
    triangle.setColor(color)
    if filled == 1:
        triangle.setFilled(True)
    else:
        triangle.setFilled(False)
    
    print(f'The area is {triangle.getArea()}')
    print(f'The perimeter is {triangle.getPerimeter()}')
    print(f'Color is {triangle.getColor()}')
    print(f'Filled is {triangle.isFilled()}')

main()