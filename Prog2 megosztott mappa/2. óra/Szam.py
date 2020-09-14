# Write a Python class to implement pow(x, n), and abs(n).

"""
Szám:
    Adattagjai:
    1. x
    2. n
    Metódusai:
    1. pow(x,n)
    2. abs(n)
"""
class Szam:

    def __init__(self,x,n):
        self.x = x
        self.n = n

    #self.x ^ self.n
    def pow(self):
        p = 1
        for i in range(self.n):
            p *= self.x
        return p

    def abs(self):
        if self.n >= 0:
            return self.n
        else:
            return -self.n

szam1 = Szam(-3,4) #példányosítottam egy Szam típusú objektumot
print("pow: ",szam1.pow())
print("abs: ",szam1.abs())