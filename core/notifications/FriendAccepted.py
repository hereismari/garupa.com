from core.notifications import Notification

class FriendAccepted(Notification):

    def __init__(self, user):
        Notification.__init__(self)

        self._user = user

    def get_type(self):
        return 'NEW_FRIEND'

    def get_data(self):
        return {
            'user': self._user.get_public_view()
        }
