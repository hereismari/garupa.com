from core.src.Notification import Notification

from datetime import datetime

class RideRequestNotification(Notification):

    def __init__(self, ride, associatedUser):
        Notification.__init__(self, {
        		'name'     : associatedUser.getName(),
        		'rideDate' : ride.getReadableDate(),
        		'Rid'      : str(ride.getRid()),
        		'Uid'	   : str(associatedUser.getUid()),
        		'type'     : 'RIDEREQUESTNOTIFICATION'
        	})

        self._ride = ride
        self._associatedUser = associatedUser
        self._message = '%s quer participar da carona do dia %s.' % (associatedUser.getName(), ride.getReadableDate())

    def getRide(self):
        return self._ride

    def getAssociatedUser(self):
        return self._associatedUser

