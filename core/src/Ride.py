from time import mktime
from datetime import date, timedelta

class Ride(object):

    # variavel estatica
    rid_counter = 1

    def __init__(self, driver, date, dest, origin, route, weekly, numberOfVacancies):

        self._driver = driver
        self._numberOfVacancies = numberOfVacancies

        self._rid = Ride.rid_counter
        Ride.rid_counter += 1

        self._date = date
        self._weekly = weekly

        self._dest = dest
        self._origin = origin
        self._route = route

        self._passengers = []

    def __eq__(self, other):
        if type(other) is not Ride: return False
        return self._rid == other.getRid()

    def __hash__(self):
        return self._rid

    def addPassenger(self, passenger, address):
        if not self.isFull() and not self.containsUser(passenger):
            self._passengers.append((passenger, address))

    def removePassenger(self, passenger):
        old_size = self.getNumberOfPassengers()

        self._passengers = [p for p in self._passengers if p[0] != passenger]
        return old_size != self.getNumberOfPassengers()

    def getNumberOfPassengers(self):
        return len(self._passengers)

    def containsUser(self, user):
        for passenger in self._passengers:
            if passenger[0] == user: return True
        return user == self._driver

    def isFull(self):
        return self.getNumberOfPassengers() == self.getNumberOfVacancies()

    def update(self):
        sunday = self.getLastSunday()
        if self.isWeekly() and self._date.date() < sunday:
            self._date += timedelta(weeks=1)
        return self._date.date() >= sunday

    def getLastSunday(self):
        today = date.today()
        weekday = today.isoweekday() % 7
        return today - timedelta(weekday)

    def happensOn(self, date):
        return abs(self._date - date) <= timedelta(minutes=15)

    """ Set and Get functions """

    def getDate(self):
        return self._date

    def getTimestamp(self):
        return mktime(self.getDate().timetuple())

    def getReadableDate(self):
        return self.getDate().strftime('%Y-%m-%d')

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

    def getRid(self):
        return self._rid

    def getDestination(self):
        return self._dest

    def getOrigin(self):
        return self._origin

    def getRoute(self):
        return self._route

    """ Get view """

    def getView(self):
        return {
            'date': int(self.getTimestamp() * 1000),

            'rid': self.getRid(),
            'driver': self.getDriver().getPublicView(),
            'dest': self.getDestination(),
            'origin': self.getOrigin(),
            'route': self.getRoute(),
            'weekly': self.isWeekly(),
            'seats': self.getNumberOfVacancies(),

            'passengers': [{
                'name': p[0].getName(),
                'uid': p[0].getUid(),
                'address': {
                    'district': p[1].getDistrict(),
                    'complement': p[1].getComplement()
                }
            } for p in self.getPassengers()]
        }
