import datetime
import math

class People(object):
   def __init__(self,name,dob):
       self.name = name
       self.date_of_birth = dob

   def __str__(self):
       return self.name + " " + self.date_of_birth

   def getAge(self):
       now = datetime.datetime.now().date()
       bd = datetime.date(int(self.date_of_birth[:4]), int(self.date_of_birth[5:7]), int(self.date_of_birth[8:10]))
       return math.trunc((int((now - bd).days) / 365))

class Student(People):
    def __init__(self,name,dob,neptuncode,specialization):
        super().__init__(name,dob)
        self.neptun = neptuncode
        self.specialization = specialization

    def __str__(self):
        return super().__str__() + " " + self.neptun + " " + self.specialization




########################################################################################
h1 = Student('Kiss Béla', '1995.10.20.', 'ZJKFZS', 'GI')
print(isinstance(h1,(People,Student)))