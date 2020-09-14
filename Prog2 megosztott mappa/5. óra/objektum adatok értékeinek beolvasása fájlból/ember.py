class IT_dolgozo:

    def __init__(self,nev,kor,nem):
        self._nev = nev
        self._kor = kor
        self._nem = nem
        self.fonokok = []

    def inputFonokok(self,fileName):
            try:
                file = open(fileName,"r")
                for str in file:
                    str = str.strip() #leszedem a sor vegerol az entert
                    tmp = str.split(";")
                    self.fonokok.append(IT_dolgozo(tmp[0],tmp[1],tmp[2]))
            except FileNotFoundError:
                print("A megadott fájl nem található!")

    def printFonokok(self):
        print("FONOKOK:")
        for f in self.fonokok:
            print(f)

    def __str__(self):
        return "{}, {}, {}".format(self._nev,self._kor,self._nem)

it = IT_dolgozo('Gabi',45,'no')
print(it)
it.printFonokok()
it.inputFonokok("data.txt")
print(it)
it.printFonokok()