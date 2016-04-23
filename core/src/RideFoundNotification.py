from Notification import Notification

from datetime import datetime

class RideFoundNotification(Notification):

    def __init__(self, ride):
        Notification.__init__(self)

        self._ride = ride

    def getRide(self):
    	return self._ride

    def getType(self):
        return 'RIDEFOUNDNOTIFICATION'

    def getData(self):
        return ride.getView()
