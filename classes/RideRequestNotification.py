class RideRequestNotification(Notification):

    def __init__(self, associatedUser=None, notificationType, status=NEW_NOTIFICATION):

        self.associatedUser = associatedUser
        self.notificationType = notificationType
        self.status = status

