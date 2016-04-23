from datetime import datetime
from Notification import Notification

class RideRequestNotification(Notification):

    def __init__(self, ride, associatedUser):
        Notification.__init__(self)

        self._ride = ride
        self._associatedUser = associatedUser

    def getRide(self):
        return self._ride

    def getAssociatedUser(self):
        return self._associatedUser

    def getType(self):
        return 'RIDE_REQUEST'

    def getData(self):
        return {
            'ride': ride.getView(),
            'user': associatedUser.getPublicoView()
        }
