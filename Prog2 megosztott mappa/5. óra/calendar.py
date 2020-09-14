class Calendar:

    months = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:31,12:31}

    def __init__(self, day = 1, month = 1, year=1990):

        if Calendar.leapyear(year):
            Calendar.months[2] = 29

        self._year = year

        if month in Calendar.months.keys():
            self._month = month
        else:
            self._month = 1

        if day <= Calendar.months[self._month] and day > 1:
            self._day = day
        else:
            self._day = 1

    def set(self,year,day,month):
        if Calendar.leapyear(year):
            Calendar.months[2] = 29

        self._year = year

        if month in Calendar.months.keys():
            self._month = month
        else:
            self._month = 1

        if day <= Calendar.months[self._month] and day > 1:
            self._day = day
        else:
            self._day = 1

    def get(self):
        if self._month < 10:
            m = "0"+str(self._month)
        else:
            m = self._month
        if self._day < 10:
            d = "0"+str(self._day)
        else:
            d = self._day
        return "{}.{}.{}.".format(self._year,m,d)

    def advence(self):
        if self._day == 31 and self._month == 12:
            self._year += 1
            self._month = 1
            self._day = 1

        elif self._day == Calendar.months[self._month]:
            self._day = 1
            self._month += 1

        else:
            self._day += 1


    def __str__(self):
        if self._month < 10:
            m = "0"+str(self._month)
        else:
            m = self._month
        if self._day < 10:
            d = "0"+str(self._day)
        else:
            d = self._day
        return "{}.{}.{}.".format(self._year,m,d)

    @staticmethod
    def leapyear(y):
        if (y%4 == 0 and y%100 != 0) or (y%400 == 0):
            return True
        return False


# cal = Calendar(28,2,1992)
# print(cal)
# cal.advence()
# print(cal)
# cal.advence()
# print(cal)
#
# cal2 = Calendar(31,12,2019)
# print(cal2)
# cal2.advence()
# print(cal2)