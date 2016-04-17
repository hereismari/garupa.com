from datetime import date

class Ride:

    def __init__(self, driver, numberOfVacancies, date=date.today(), weekly=False):

        self._driver = driver
        self._numberOfVacancies = numberOfVacancies
        self._date = date
        self._weekly = weekly

        self._passengers = []

    def addPassenger(self, passenger, address):
        if not self.isFull() and not (passenger,address) in self._passengers:
            self._passengers.append((passenger, address))

    def removePassenger(self, passenger):
        result = False
        for i in xrange(len(self._passengers)):
            if self._passengers[i][0] == passenger:
                self._passengers.remove((self._passengers[i][0], self._passengers[i][1]))
                result = True
                break

        return result

    def numberOfPassengers(self):
        return len(self._passengers)

    def isFull(self):
        return len(self._passengers) == self._numberOfVacancies

    """ Set and Get functions """

    def getDate(self):
        return self._date

    def getDriver(self):
        return self._driver

    def isWeekly(self):
        return self._weekly

    def setWeekly(self, weekly):
        self._weekly = weekly

    def getNumberOfVacancies(self):
        return self._numberOfVacancies

    def setNumberOfVacancies(self, numberOfVacancies):
        self._numberOfVacancies = numberOfVacancies

    def getPassengers(self):
        return self._passengers
