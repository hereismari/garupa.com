from datetime import datetime
from Notification import Notification

class NewFriendNotification(Notification):

    def __init__(self, associatedUser):
        Notification.__init__(self)

        self._associatedUser = associatedUser
        self._message = "aceitou seu pedido de amizade"

    def getType(self):
        return 'NEW_FRIEND'

    def getAssociatedUser(self):
    	return self._associatedUser

    def getData(self):
        result = {}

        result['status'] = self.getSeen()
        result['type'] = self.getType()
        result['date'] = int(self.getTimestamp() * 1000)
        result['message'] = self.getMessage()
        result['ride'] = ""
        result['associatedUser'] = self.getAssociatedUser().getPublicView()

        return result
