"""
Write a Python class named Circle constructed by a radius and two
methods which will compute the area and the perimeter of a circle.
"""
import math

class Circle:

    def __init__(self,r):
        self.r = r

    def terulet(self):
        return self.r**2*math.pi

    def kerulet(self):
        return self.r*2*math.pi


kor = Circle(10)
print("K: ",kor.kerulet())
print("T: ",kor.terulet())