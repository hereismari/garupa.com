class RideFoundNotification(Notification):

    def __init__(self, date, ride, status=NotificationStatus.new):
        super(RideFoundNotification, self).__init__(date, status)
        self._ride = ride

    def getRide(self):
        return self._ride
