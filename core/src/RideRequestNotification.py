from core.src.Notification import Notification
from core.src.NotificationStatus import NotificationStatus

from time import time

class RideRequestNotification(Notification):

    def __init__(self, ride, associatedUser, date=int(time()*1000), status=NotificationStatus.new):
        Notification.__init__(self, date, status)
        self._ride = ride
        self._associatedUser = associatedUser
        self._message = '%s quer participar da carona do dia %s.' % (associatedUser.getName(), str(ride.getReadableDate()))

    def getRide(self):
        return self._ride

    def getAssociatedUser(self):
        return self._associatedUser
