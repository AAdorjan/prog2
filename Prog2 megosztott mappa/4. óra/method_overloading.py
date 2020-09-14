def greeting(name = None):
    '''Metódus túlterhelés példa. A függvény ilyesfajta specifikációja megadja számunkra
    azt a lehetőséget, hogy a greeting() függvényt meghívjuk különböző paraméterlistával'''
    if name == None:
        print("Hello")
    else:
        print("Hello " + name)

greeting('John')
greeting()