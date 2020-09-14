"""A Rational is represented by two integers, the numerator and the denominator.
You can apply many of the numeric operators to Rational. """

class Fraction:

    def __init__(self,numerator,denominator):
        self.n  = numerator
        self.d = denominator

    def __str__(self):
        return "{}/{}".format(self.n,self.d)

    def __add__(self, other):
        if self.d == other.d:
            return Fraction(self.n+other.n,self.d)
        else:
            common_denom = Fraction.lcm(self.d,other.d)
            a = (common_denom/self.d)*self.n
            b = (common_denom/other.d)*other.n
            return Fraction(int(a+b),common_denom)

    def __sub__(self, other):
        if self.d == other.d:
            return Fraction(self.n-other.n,self.d)
        else:
            common_denom = Fraction.lcm(self.d, other.d)
            a = (common_denom / self.d) * self.n
            b = (common_denom / other.d) * other.n
            return Fraction(int(a - b), common_denom)

    def __mul__(self, other):
        return Fraction(self.n*other.n,self.d*other.d)


    @staticmethod
    def lcm(x, y):
        if x > y:
            greater = x
        else:
            greater = y

        while (True):
            if ((greater % x == 0) and (greater % y == 0)):
                lcm = greater
                break
            greater += 1

        return lcm

fr1 = Fraction(4,6)
fr2 = Fraction(1,6)
fr3 = Fraction(2,3)
fr4 = Fraction(4,5)
print(fr3+fr4)
print(fr4-fr3)
print(fr1*fr2)