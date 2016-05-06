from core.src.Notification import Notification

class RideRequestAcceptedNotification(Notification):

    def __init__(self, ride, associatedUser):
        Notification.__init__(self)

        self._ride = ride
        self._associatedUser = associatedUser

    def get_type(self):
        return 'RIDE_REQUEST_ACCEPTED'

    def get_data(self):
        return {
		'ride' : self._ride.get_view()
        'user' : self._associatedUser.get_public_view()
	}

