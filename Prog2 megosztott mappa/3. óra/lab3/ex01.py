# Write a Python class named Triangle constructed by the three side length.
# The class contains methods which calculates the perimeter and
# the area from the known information. Overload the addition, subtraction,
# equality, greater/less than or equal and not equal operators.
import math

class Triangle:

    def __init__(self,szam1,szam2,szam3):
    """Egy háromszög 3 oldalának értékének megadása"""
        self.a = szam1
        self.b = szam2
        self.c = szam3

    def kerulet(self): #perimeter = kerulet
        return self.a + self.b + self.c

    def terulet(self): #area = terulet (Heron-képlet)
        p = (self.a+self.b+self.c)/2
        return math.sqrt(p*(p-self.a)*(p-self.b)*(p-self.c))

    def __add__(self, other):
    """A + operátor felülírása 2 háromszög objektum esetén. 
    Mit jelent az, hogy két háromszöget összeadunk? Attól függ mit kér a feladat.
    Órán úgy fogalmaztuk meg, két háromszög összeadása azt jelenti, hogy páronként összeadjuk
    az azonos oldalakat és így megkapunk 3 új értéket. Ezekből az értékekből létrehozunk egy új háromszög
    objektumot, és azt visszaadjuk"""
        uj_haromszog = Triangle(self.a+other.a,self.b+other.b,self.c+other.c)
        return uj_haromszog

    def __sub__(self, other):
    """Kivonás esetén hasonlóan gondolkodtunk. Annyi a különbség, ha kivonjuk egyik 'a' oldalból a másik 'a' oldalt,
vagy 'b'-ből 'b'-t vagy 'c'-ből 'c'-t, lehetséges hogy negatív számot kapunk eredményül. Az if feltételben azt adtuk meg,
ha ezek közül a kivonások közül valamelyik eredménye 0 vagy annál kisebb szám, akkor egy olyan háromszög kerüljön visszaadásra,
melynek minden oldala 0 hosszú. (nyilván ezek nem értelmes értékek egy háromszög esetén, de ezzel az volt a célunk, hogy
jelezzük a felhasználónak maga a kivonás művelet nem értelmezhető ebben az esetben. """     
        a = self.a - other.a
        b = self.b - other.b
        c = self.c - other.c

        if (a or b or c) <= 0:
            return Triangle(0,0,0)
        else:
            uj_haromszog = Triangle(a,b,c)
            return uj_haromszog

    def __eq__(self, other):
    """Egy háromszög akkor egyezik meg, ha az azonos oldalak hossza megegyezik."""
        if self.a == other.a and self.b == other.b and self.c == other.c:
            return True
        return False

    def __gt__(self, other):
        if self.a > other.a and self.b > other.b and self.c > other.c:
            return True
        else:
            return False

    def __lt__(self, other):
        if self.a < other.a and self.b < other.b and self.c < other.c:
            return True
        else:
            return False

    def __str__(self):
            return "A haromszog oldalai: a = {} b = {} c = {}".format(str(self.a),str(self.b),str(self.c))

#######################################################################################
h1 = Triangle(24,16.9,28.9)
h2 = Triangle(11,6,6)
h3 = Triangle(11,6,6)
print("h1 kerulete: ",h1.kerulet())
print("h1 terulete: ",h1.terulet())

# if h3 == h2:
#     print("A két háromszög összes oldala megegyezik")
# else:
#     print("Valamely oldala a háromszögeknek nem egyezik meg")

# if h1 > h2:
#     print("Az első háromszög minden oldala nagyobb mint a másodiké")
# else:
#     print("Valamely oldala az első háromszögnek kisebb (vagy egyenlő) mint a másodiké")

# if h2 < h1:
#     print("Az első háromszög minden oldala kisebb mint az elsőé")
# else:
#     print("Valamely oldala az első háromszögnek nagyobb (vagy egyenlő) mint a másodiké")
#
#
# eredmeny_hsz_kiv = h2 - h1
# print(eredmeny_hsz_kiv)
#
# eredmeny_hsz_ossz = h2 + h3
# print(eredmeny_hsz_ossz)



