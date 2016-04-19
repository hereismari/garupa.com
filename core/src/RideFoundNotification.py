from Notification import Notification
from NotificationStatus import NotificationStatus

from time import time

class RideFoundNotification(Notification):

    def __init__(self, ride, date=int(time()*1000), status=NotificationStatus.new):
        Notification.__init__(self, date, status)
        self._ride = ride
        self._message = 'Uma carona na data %s surgiu.' % (str(ride.getReadableDate()))

    def getRide(self):
        return self._ride

