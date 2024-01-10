'''
Avni Gandhi
CIS 41A, Spring 2023
Unit I, Exercise I
'''
import math
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def getArea(self):
        return math.pi * self.radius**2
        

class Cylinder(Circle):
    def __init__(self, radius, height):
        super().__init__(radius)
        self.height = height

    def getVolume(self):
        return self.getArea()*self.height
    
circle = Circle(4)
print("Circle area is: %.2f" %circle.getArea())
cylinder = Cylinder(2,5)
print("Cylinder volume is: %.2f" %cylinder.getVolume())

'''
Execution results:
Circle area is: 50.27
Cylinder volume is: 62.83
'''
