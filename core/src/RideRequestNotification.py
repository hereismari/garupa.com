from datetime import datetime
from Notification import Notification

class RideRequestNotification(Notification):

    def __init__(self, ride, associatedUser):
        Notification.__init__(self)

        self._ride = ride
        self._associatedUser = associatedUser
        self._message = "quer participar de uma carona"

    def getRide(self):
        return self._ride

    def getAssociatedUser(self):
        return self._associatedUser

    def getType(self):
        return 'RIDE_REQUEST'

    def getData(self):
        result = {}

        result['status'] = self.getSeen()
        result['type'] = self.getType()
        result['date'] = self.getReadableDate()
        result['message'] = self.getMessage()
        result['ride'] = ride.getView()
        result['associatedUser'] = self.getAssociatedUser().getPublicView()

        return result
