from Notification import Notification

from datetime import datetime

class NewFriendNotification(Notification):

    def __init__(self, associatedUser):
        Notification.__init__(self, {
        		'name' : associatedUser.getName(),
        		'Uid'  : str(associatedUser.getUid()),
        		'type' : 'NEWFRIENDNOTIFICATION'
        	})

        self._associatedUser = associatedUser
        self._message = '%s aceitou seu pedido de amizade.' % (associatedUser.getName())

    def getAssociatedUser(self):
    	return self._associatedUser