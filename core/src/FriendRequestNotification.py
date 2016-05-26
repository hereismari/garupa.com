from Notification import Notification

class FriendRequestNotification(Notification):

    def __init__(self, user):
        Notification.__init__(self)

        self._user = user

    def getType(self):
        return 'FRIEND_REQUEST'

    def getData(self):
        return {
            'user': self._user.getPublicView()
        }
