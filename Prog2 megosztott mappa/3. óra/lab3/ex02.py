# Write a Python class named Vector constructed by the x and y coordinates of the endpoint.
# Configure abs() to return the length of vector.
# It is possible to add, subtract and multiply any two vectors or real number.
# Compare two vectors based on their lengths.
import math

class Vector:

    def __init__(self,vx,vy):
        self.x = vx
        self.y = vy

    def abs(self):
        return math.sqrt(self.x**2 + self.y**2)

    def __add__(self, other):
        uj_vektor = Vector(self.x+other.x,self.y+other.y)
        return uj_vektor

    def __sub__(self, other):
        uj_vektor = Vector(self.x-other.x,self.y-other.y)
        return uj_vektor

    def __mul__(self, other): #belső szorzat
        belso_szorzat = (self.x*other.x)+(self.y*other.y)
        return belso_szorzat

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.x > other.x and self.y > other.y:
            return True
        return False

    def __lt__(self,other):
        if self.x < other.x and self.y < other.y:
            return True
        return False
    
v1 = Vector(5,5)
v2 = Vector(10,11)
print(v1.abs())