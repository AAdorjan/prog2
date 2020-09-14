"""
Write a Python class named Rectangle constructed by a length and width and
a method which will compute the area of a rectangle.
"""

class Rectangle:

    def __init__(self,a,b):
        self.a = a
        self.b = b

    def terulet(self):
        return self.a*self.b

    def kerulet(self):
        return 2*(self.a+self.b)


t = Rectangle(10,10)
print("K: ",t.kerulet())
print("T: ",t.terulet())