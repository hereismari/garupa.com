from Notification import Notification

class RideRequestAcceptedNotification(Notification):

    def __init__(self, ride, user):
        Notification.__init__(self)

        self._ride = ride
        self._user = user

    def getType(self):
        return 'RIDE_ACCEPTED'

    def getData(self):
        return {
            'user': self._user.getPublicView(),
            'ride': self._ride.getView()
        }
