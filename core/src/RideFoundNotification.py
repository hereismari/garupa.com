from Notification import Notification

from datetime import datetime

class RideFoundNotification(Notification):

    def __init__(self, ride, date=datetime.now(), status=False):
        Notification.__init__(self, date, status)
        self._ride = ride
        self._message = 'Uma carona na data %s surgiu.' % (str(ride.getReadableDate()))

    def getRide(self):
        return self._ride

