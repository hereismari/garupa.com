from core.src.Notification import Notification
from core.src.NotificationStatus import NotificationStatus
from datetime import date

class FriendRequestNotification(Notification):

    def __init__(self, associatedUser, date=date.today(), status=NotificationStatus.new):
        Notification.__init__(self, date, status)
        self._associatedUser = associatedUser
        self._message = '%s quer ser seu amigo.' % (associatedUser.getName())

    def getAssociatedUser(self):
        return self._associatedUser
