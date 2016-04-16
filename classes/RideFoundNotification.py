from datetime import date

class RideFoundNotification(Notification):

    def __init__(self, date, rideDate, status=NotificationStatus.new):
        super(RideFoundNotification, self).__init__(date, status)
        self._rideDate = rideDate

