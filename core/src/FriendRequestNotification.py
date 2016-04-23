from datetime import datetime
from Notification import Notification

class FriendRequestNotification(Notification):

    def __init__(self, associatedUser):
        Notification.__init__(self)

        self._associatedUser = associatedUser

    def getAssociatedUser(self):
    	return self._associatedUser

    def getType(self):
        return 'FRIEND_REQUEST'

    def getData(self):
        return associatedUser.getPublicView()
