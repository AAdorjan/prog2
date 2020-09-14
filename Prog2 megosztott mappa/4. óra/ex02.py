class Account():

    minimum_balance = 100000

    def __init__(self,balance):
        self.b  = balance

    def deposit(self,amount):
        #készpénz letétbe helyezés
        self.b += amount
        print("Tranzakció sikeres! Letétbe helyezett összeg: {}. Új egyenleg: {}".format(amount,self.b))

    def withdrawal(self,amount):
        #készpénz felvétel
        if self.b - amount < Account.minimum_balance:
            print("A tranzakció nem hajtható végre. A megadott összeg felvételével nem marad elegendő összeg a számlán.")
        else:
            self.b -= amount
            print("Tranzakció sikeres! Letétbe helyezett összeg: {}. Új egyenleg: {}".format(amount,self.b))

    def __str__(self):
        return "Egyenleg: {}".format(self.b)

acc = Account(150000)
acc.deposit(150)
acc.withdrawal(60000)
print(acc)