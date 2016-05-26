from Notification import Notification

class RideRequestNotification(Notification):

    def __init__(self, ride, user, district, complement):
        Notification.__init__(self)

        self._ride = ride
        self._user = user
        self._district = district
        self._complement = complement

    def getType(self):
        return 'RIDE_REQUEST'

    def getData(self):
        return {
            'ride': self._ride.getView(),
            'user': self._user.getPublicView(),
            'district': self._district,
            'complement': self._complement
        }
