from Notification import Notification
from NotificationStatus import NotificationStatus

from time import time

class FriendRequestNotification(Notification):

    def __init__(self, associatedUser, date=int(time()*1000), status=NotificationStatus.new):
        Notification.__init__(self, date, status)
        self._associatedUser = associatedUser
        self._message = '%s quer ser seu amigo.' % (associatedUser.getName())

    def getAssociatedUser(self):
        return self._associatedUser
