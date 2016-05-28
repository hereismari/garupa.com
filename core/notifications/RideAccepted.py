from core.notifications import Notification
from core.database import db

class RideAccepted(Notification):

    _nid = db.Column('nid', db.Integer, db.ForeignKey('notification.nid'), primary_key=True)

    _user = db.relationship('User')
    _user_id = db.Column(db.ForeignKey('user.uid'))

    _ride = db.relationship('Ride')
    _ride_id = db.Column(db.ForeignKey('ride.rid'))


    __tablename__ = 'notification$ride_accepted'

    __mapper_args__ = {
        'polymorphic_identity': 'ride_accepted'
    }


    def __init__(self, ride, user):
        Notification.__init__(self)

        self._ride = ride
        self._user = user

    def get_type(self):
        return 'RIDE_ACCEPTED'

    def get_data(self):
        return {
            'user': self._user.get_public_view(),
            'ride': self._ride.get_view()
        }
