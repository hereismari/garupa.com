from core.src.Notification import Notification

class RideRequestAcceptedNotification(Notification):

    def __init__(self, ride, associatedUser):
        Notification.__init__(self)

        self._ride = ride
        self._associatedUser = associatedUser

    def getRide(self):
        return self._ride

    def getAssociatedUser(self):
        return self._associatedUser

    def getType(self):
        return 'RIDEREQUESTACCEPTEDNOTIFICATION'

    def getData(self):
        return {
		'ride' : ride.getView()
                'user' : associatedUser.getPublicoView()
	}

