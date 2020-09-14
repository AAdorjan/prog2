class Clock:

    def __init__(self, hours = 0, mins = 0, secs = 0):
        if hours in [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]:
            self._hours = hours
        else:
            print("Az _hours értéke nem megfelelő")
            self._hours = 0
        if mins < 60 and mins >= 0:
            self._mins = mins
        else:
            print("A _mins értéke nem megfelelő")
            self._mins = 0
        if secs < 60 and secs >= 0:
            self._secs = secs
        else:
            print("A _secs értéke nem megfelelő")
            self._secs = 0


    def set(self,hours,mins,secs):
        if hours in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]:
            self._hours = hours
        else:
            print("Az _hours értéke nem megfelelő")
            self._hours = 0
        if mins < 60 and mins >= 0:
            self._mins = mins
        else:
            print("A _mins értéke nem megfelelő")
            self._mins = 0
        if secs < 60 and secs >= 0:
            self._secs = secs
        else:
            print("A _secs értéke nem megfelelő")
            self._secs = 0

    def display(self):
        if self._hours < 10:
            h = "0"+str(self._hours)
        else:
            h = self._hours
        if self._mins < 10:
            m = "0"+str(self._mins)
        else:
            m = self._mins
        if self._secs < 10:
            s = "0"+str(self._secs)
        else:
            s = self._secs

        return "{}:{}:{}".format(h,m,s)
    def __str__(self):
        return "{}:{}:{}".format(self._hours,self._mins,self._secs)

    def tick(self):
        """ 1 mp-el növeljük az időt"""
        if self._secs == 59 and self._mins == 59 and self._hours == 23:
            self._secs = 0
            self._mins = 0
            self._hours = 0

        elif self._secs == 59 and self._mins == 59:
            self._secs = 0
            self._mins = 0
            self._hours += 1

        elif self._secs == 59:
            self._secs = 0
            self._mins += 1

        else:
            self._secs+=1



#
# c = Clock(22,5,5)
# print(c)
# c.set(22,59,59)
# print(c)
# c.tick()
# print(c)
# print(c.display())