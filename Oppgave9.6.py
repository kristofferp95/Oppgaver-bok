import math

class QuadraticEquation: 
    def __init__(self, a = 1.0, b = 1.0, c = 1.0):
        self.__a = a 
        self.__b = b
        self.__c = c 

    def getA(self):
        return self.__a
    
    def setA(self, a):
        self.__a = a
    
    def getB(self):
        return self.__b
    
    def setB(self, b): 
        self.__b = b
    
    def getC(self): 
        return self.__c
    
    def setC(self, c): 
        self.__c = c
    
    def getDiscriminant(self): 
        d = (self.__b * self.__b - (4 * self.__a * self.__c))
        return d

    def getRoot1(self): 
        k = (-self.__b + math.sqrt(self.__b*self.__b - (4 * self.__a * self.__c))) / 2 * self.__a

        return k
    
    def getRoot2(self): 
        z = (-self.__b - math.sqrt(self.__b*self.__b - (4 * self.__a * self.__c))) / 2 * self.__a
    
        return z


def main(): 
    a = float(input(f'Enter a value for A: '))
    b = float(input(f'Enter a value for B: '))
    c = float(input(f'Enter a value for C: '))
    roots = QuadraticEquation(a, b, c)
    if roots.getDiscriminant() < 0: 
        print(f'The equation has no roots')
    elif roots.getDiscriminant() == 0: 
        print(f'Root: {roots.getRoot1()}')
    else: 
        print(f'Roots: {roots.getRoot1()} and {roots.getRoot2()}')

main()
