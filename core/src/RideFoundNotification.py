from Notification import Notification

from datetime import datetime

class RideFoundNotification(Notification):

    def __init__(self, ride):
        Notification.__init__(self, {
        		'readableDate' : ride.getReadableDate(),
        		'driver' 	   : ride.getDriver().getName(),
        		'Rid'  		   : str(ride.getRid()),
        		'Uid'          : str(ride.getDriver().getUid()),
        		'type'		   : 'RIDEFOUNDNOTIFICATION'
        	})

        self._ride = ride
        self._message = 'Uma carona na data %s surgiu.' % (ride.getReadableDate())

    def getRide(self):
    	return self._ride
