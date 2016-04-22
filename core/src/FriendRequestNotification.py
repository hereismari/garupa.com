from Notification import Notification

from datetime import datetime

class FriendRequestNotification(Notification):

    def __init__(self, associatedUser):
        Notification.__init__(self, {
        		'name' : associatedUser.getName(),
        		'Uid'  : str(associatedUser.getUid()),
        		'type' : 'FRIENDREQUESTNOTIFICATION'
        	})

        self._associatedUser = associatedUser
        self._message = '%s quer ser seu amigo.' % (associatedUser.getName())

    def getAssociatedUser(self):
    	return self._associatedUser
