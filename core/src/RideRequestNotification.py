from core.src.Notification import Notification

from datetime import datetime

class RideRequestNotification(Notification):

    def __init__(self, ride, associatedUser, date=datetime.now(), status=False):
        Notification.__init__(self, date, status)
        self._ride = ride
        self._associatedUser = associatedUser
        self._message = '%s quer participar da carona do dia %s.' % (associatedUser.getName(), str(ride.getReadableDate()))

    def getRide(self):
        return self._ride

    def getAssociatedUser(self):
        return self._associatedUser

