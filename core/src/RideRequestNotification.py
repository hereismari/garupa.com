
class RideRequestNotification(Notification):

    def __init__(self, date, associatedUser, ride, status=NotificationStatus.new):
        super(RideFoundNotification, self).__init__(date, status)
        self._associatedUser = associatedUser
        self._ride = ride

    def getRide(self):
        return self._ride

    def getAssociatedUser(self):
        return self._associatedUser

