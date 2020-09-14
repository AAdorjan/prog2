import math

class Polygon:
    def __init__(self):
        self.num_of_sides = 0#oldalak száma
        self.magnitudes = [] #oldalak hossza

    def inputSides(self):
        '''
        Method inputSides() takes in magnitude of each side
        '''
        self.magnitudes = input('Give the length of each side (separated by a space character): ').split(' ')
        self.num_of_sides = len(self.magnitudes)

    def dispSides(self):
        '''
        dispSides() displays the length of each side
        '''
        return self.magnitudes

    def __str__(self):
        return "Number of sides: {}, Length of each side: {}".format(self.num_of_sides,self.magnitudes)

class Triangle(Polygon):

    def getArea(self):
        if len(self.magnitudes) != 3:
            print("You gave too many or too less input parameters for a Triangle object. The number of sides in case of a Triangle must be 3!")
            return
        s = (float(self.magnitudes[0]) + float(self.magnitudes[1]) + float(self.magnitudes[2]))/2
        return math.sqrt(s*(s-float(self.magnitudes[0]))*(s-float(self.magnitudes[1]))*(s-float(self.magnitudes[2])))

    def getPerimeter(self):
        if len(self.magnitudes) != 3:
            print("You gave too many or too less input parameters for a Triangle object. The number of sides in case of a Triangle must be 3!")
            return
        return float(self.magnitudes[0]) + float(self.magnitudes[1]) + float(self.magnitudes[2])


# p1 = Polygon()
# p1.inputSides()
# print(p1)
t1 = Triangle()
t1.inputSides()
print('The perimeter of t1 is {}'.format(t1.getPerimeter()))
print('The area of t1 is {}'.format(t1.getArea()))