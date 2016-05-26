from core.notifications import Notification

class RideRequest(Notification):

    def __init__(self, ride, user, district, complement):
        Notification.__init__(self)

        self._ride = ride
        self._user = user
        self._district = district
        self._complement = complement

    def get_type(self):
        return 'RIDE_REQUEST'

    def get_data(self):
        return {
            'ride': self._ride.get_view(),
            'user': self._user.get_public_view(),
            'district': self._district,
            'complement': self._complement
        }
