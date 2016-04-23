from datetime import datetime
from Notification import Notification

class RideFoundNotification(Notification):

    def __init__(self, ride):
        Notification.__init__(self)

        self._ride = ride

    def getRide(self):
    	return self._ride

    def getType(self):
        return 'RIDE_FOUND'

    def getData(self):
        return ride.getView()
