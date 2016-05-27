from core.notifications import Notification

class RideAccepted(Notification):

    def __init__(self, ride, user):
        Notification.__init__(self)

        self._ride = ride
        self._user = user

    def get_type(self):
        return 'RIDE_ACCEPTED'

    def get_data(self):
        return {
            'user': self._user.get_public_view(),
            'ride': self._ride.get_view()
        }
