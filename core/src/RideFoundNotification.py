from Notification import Notification

class RideFoundNotification(Notification):

    def __init__(self, ride):
        Notification.__init__(self)

        self._ride = ride

    def getType(self):
        return 'RIDE_FOUND'

    def getData(self):
        return {
            'ride': self._ride.getView()
        }
