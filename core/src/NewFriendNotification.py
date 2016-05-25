from Notification import Notification

class NewFriendNotification(Notification):

    def __init__(self, user):
        Notification.__init__(self)

        self._user = user

    def getType(self):
        return 'NEW_FRIEND'

    def getData(self):
        return {
            'user': self._user.getPublicView()
        }
