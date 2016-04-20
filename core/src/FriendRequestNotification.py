from Notification import Notification

from time import time

class FriendRequestNotification(Notification):

    def __init__(self, associatedUser, date=int(time()*1000), status=False):
        Notification.__init__(self, date, status)
        self._associatedUser = associatedUser
        self._message = '%s quer ser seu amigo.' % (associatedUser.getName())

    def getAssociatedUser(self):
        return self._associatedUser

