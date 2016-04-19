from core.src.Notification import Notification
from core.src.NotificationStatus import NotificationStatus
from datetime import date

class RideFoundNotification(Notification):

    def __init__(self, ride, date=date.today(), status=NotificationStatus.new):
        Notification.__init__(self, date, status)
        self._ride = ride
        self._message = 'Uma carona na data %s surgiu.' % (str(ride.getDate()))

    def getRide(self):
        return self._ride

