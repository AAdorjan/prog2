# Implement our own class to represent complex numbers.The constructor takes two arguments,
# representing the real and imaginary parts of the complex number.Define two methods inside
# the class, conjugate() and argz(), which will give us the complex conjugate and the argument
# of a complex number.Configure abs() to return the modulus of a complex number.It is possible
# to add any two complex numbers or add a real number to a complex number.Let’s configure
# the + operator in such a way that it works for both cases.Similarly,
# you define the behavior for - and *.Now, we take care of the two operators,
# == and !=.It is also possible to raise a complex number to any power.

class Complex:

    def __init__(self,real,imag):
        self.r = real #valós
        self.i = imag #képzetes rész

    def conjugate(self):
        if '+' in self.i:
           self.i = self.i.replace("+","-")
        else:
           self.i = self.i.replace("-", "+")

    def __str__(self):
        return "{}{}".format(self.r,self.i)

    def argz(self):
        pass

c1 = Complex(5,'+4i')
print(c1)
c1.conjugate()
print(c1)