from time import time
from datetime import datetime

class Ride:

    # variavel estatica
    uid_counter = 1

    def __init__(self, driver, numberOfVacancies, date = int(time()*1000), weekly=False):

        self._driver = driver
        self._numberOfVacancies = numberOfVacancies
        
        self._uid = Ride.uid_counter
        Ride.uid_counter += 1
    
        self._date = date
        self._weekly = weekly

        self._passengers = []

    def addPassenger(self, passenger, address):
        if not self.isFull() and passenger != self._driver and not self.containsPassenger(passenger):
            self._passengers.append((passenger, address))

    def removePassenger(self, passenger):
        old_size = self.getNumberOfPassengers()

        self._passengers = [p for p in self._passengers if p[0] != passenger]
        return old_size != self.getNumberOfPassengers()
    
    def getNumberOfPassengers(self):
        return len(self._passengers)

    def containsPassenger(self, user):
        for passenger in self._passengers:
            if passenger[0] == user: return True
        return False
    
    def isFull(self):
        return (self.getNumberOfPassengers() == self.getNumberOfVacancies())

    def __eq__(self, otherRide):
        return self.getUid() == otherRide.getUid()

    """ Set and Get functions """

    def getDate(self):
        return self._date

    def setDate(self, timestamp):
        self._date = timestamp

    def getReadableDate(self):
        return datetime.fromtimestamp(self.getDate()/1000).strftime('%Y-%m-%d')

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

    def getUid(self):
        return self._uid
    
    """ Get view """

    def getView(self):
        result = {}
        result['weekly'] = self.isWeekly()
        result['date'] = str(self.getDate())
        result['driver'] = self.getDriver().getName()
        result['number_of_vacancies'] = self.getNumberOfVacancies()
        for passenger in self.getPassengers:
            result['passengers'].append(passenger.getName())
        return result
