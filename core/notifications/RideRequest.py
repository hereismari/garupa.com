from core.notifications import Notification
from core.database import db

class RideRequest(Notification):

    _nid = db.Column('nid', db.Integer, db.ForeignKey('notification.nid'), primary_key=True)

    _user = db.relationship('User')
    _user_id = db.Column(db.ForeignKey('user.uid'))

    _ride = db.relationship('Ride')
    _ride_id = db.Column(db.ForeignKey('ride.rid'))

    _district = db.Column('district', db.String(30))
    _complement = db.Column('complement', db.String(30))


    __tablename__ = 'notification$ride_request'

    __mapper_args__ = {
        'polymorphic_identity': 'ride_request'
    }


    def __init__(self, ride, user, district, complement):
        Notification.__init__(self)

        self._ride = ride
        self._user = user
        self._district = district
        self._complement = complement

    def get_type(self):
        return 'RIDE_REQUEST'

    def get_data(self):
        return {
            'ride': self._ride.get_view(),
            'user': self._user.get_public_view(),
            'district': self._district,
            'complement': self._complement
        }
