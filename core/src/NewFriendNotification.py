from datetime import datetime
from Notification import Notification

class NewFriendNotification(Notification):

    def __init__(self, associatedUser):
        Notification.__init__(self)

        self._associatedUser = associatedUser

    def getType(self):
        return 'NEW_FRIEND'

    def getAssociatedUser(self):
    	return self._associatedUser

    def getData(self):
        return associatedUser.getPublicView()
