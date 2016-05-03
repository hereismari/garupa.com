from core.src.Notification import Notification

class RideRequestAcceptedNotification(Notification):

    def __init__(self, ride, associatedUser):
        Notification.__init__(self)

        self._ride = ride
        self._associatedUser = associatedUser
        self._message = "aceitou seu pedido de carona"

    def getRide(self):
        return self._ride

    def getAssociatedUser(self):
        return self._associatedUser

    def getType(self):
        return 'RIDE_ACCEPTED'

    def getData(self):
        result = {}

        result['status'] = self.getSeen()
        result['type'] = self.getType()
        result['date'] = self.getReadableDate()
        result['message'] = self.getMessage()
        result['ride'] = self.getRide().getView()
        result['associatedUser'] = self.getAssociatedUser().getPublicView()

        return result
