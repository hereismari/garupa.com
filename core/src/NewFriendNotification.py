class RideFoundNotification(Notification):

    def __init__(self, date, associatedUser, status=NotificationStatus.new):
        super(RideFoundNotification, self).__init__(date, status)
        self._associatedUser = associatedUser

