class Ride:

    def __init__(self, driver, numberOfVacancies, weekly=False):

        self._driver = driver
        self._weekly = weekly
        self._numberOfVacancies = numberOfVacancies

        self._passengers = []

    def addPassenger(self, passenger, address):
        if not isFull():
            self.passengers.append((passenger, address))

    def removePassenger(self, passenger):
        bool result = False
        for i in range(len(passengers)):
            if passengers[i][0] == passenger:
                self.passengers.remove(i)
                result = True

        return result

    def isFull(self):
        return len(passengers) == numberOfVacancies

    """ Set and Get functions """

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
