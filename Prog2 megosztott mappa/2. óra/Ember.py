"""
Ember osztály:
Minden ember rendelkezik az alábbi attribútumokkal (adattag/mező):
1. Név
2. Életkor
3. Nem

Minden emberről megállapítható, hogy idős-e. Egy embert idősnek tekintünk, ha idősebb, mint 65.

"""

class Ember:

    def __init__(self,nev,kor,nem):
        self.nev = nev
        self.kor = kor
        self.nem = nem

    #igazat, adjon vissza ha a kor > 65 hamisat egyébként
    """
    Példánymetódus: egy adott objektumra (példány) vonatkozik a metódus
    Az adott objektum adattagjaival dolgozik (self). 
    """
    def idos_e(self):
        return self.kor > 65
        # if self.kor > 65:
        #     return True
        # else:
        #     return False

    """
    Osztálymetódus: (@staticmethod)
    Nem egy adott objektumra vonatkozik a metódus.
    Tehát nincs szükség a self paraméterre, mert nem egy adott
    objektum adattagjaival számolunk. 
    """
    @staticmethod
    def legidosebb(lista):
        max = 0
        for e in lista:
            if e.kor > max:
                max = e.kor
                max_nev = e.nev
        return max_nev


e = Ember("XY",20,True) #példányosítás
print("Név: ",e.nev)
print("Kor: ",e.kor)
print("Nem: ",e.nem)
print("e idős-e?: ",e.idos_e())
#-------------------------------------------------------------------------------

lista = []
lista.append(e)
lista.append(Ember("AB",21,False))
lista.append(Ember("DE",22,False))
lista.append(Ember("IJK",20,True))

#osztálymetódus meghívása: Osztálynév.metódusnév()
print("Legidősebb: ",Ember.legidosebb(lista))