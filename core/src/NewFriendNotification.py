from datetime import datetime
from Notification import Notification

class NewFriendNotification(Notification):

    def __init__(self, associatedUser):
        Notification.__init__(self)

        self._associatedUser = associatedUser

    def get_type(self):
        return 'NEW_FRIEND'

    def get_data(self):
        return self._associatedUser.get_public_view()
