from datetime import datetime
from Notification import Notification

class NewFriendNotification(Notification):

    def __init__(self, nid, associatedUser):
        Notification.__init__(self, nid)

        self._associatedUser = associatedUser
        self._message = "aceitou seu pedido de amizade"

    def getType(self):
        return 'NEW_FRIEND'

    def getAssociatedUser(self):
    	return self._associatedUser

    def getData(self):
        result = {}

        result['nid'] = self.getNid()
        result['status'] = self.getSeen()
        result['type'] = self.getType()
        result['date'] = self.getReadableDate()
        result['message'] = self.getMessage()
        result['ride'] = ""
        result['associatedUser'] = self.getAssociatedUser().getPublicView()

        return result
