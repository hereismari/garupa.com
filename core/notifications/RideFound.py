from core.notifications import Notification
from core.database import db

class RideFound(Notification):

    _nid = db.Column('nid', db.Integer, db.ForeignKey('notification.nid'), primary_key=True)

    _ride = db.relationship('Ride')
    _ride_id = db.Column(db.ForeignKey('ride.rid'))


    __tablename__ = 'notification$ride_found'

    __mapper_args__ = {
        'polymorphic_identity': 'ride_found'
    }


    def __init__(self, ride):
        Notification.__init__(self)

        self._ride = ride

    def get_type(self):
        return 'RIDE_FOUND'

    def get_data(self):
        return {
            'ride': self._ride.get_view()
        }
