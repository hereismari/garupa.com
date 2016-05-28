from core.notifications import Notification
from core.database import db

class FriendRequest(Notification):

    _nid = db.Column('nid', db.Integer, db.ForeignKey('notification.nid'), primary_key=True)

    _user = db.relationship('User')
    _user_id = db.Column(db.ForeignKey('user.uid'))


    __tablename__ = 'notification$friend_request'

    __mapper_args__ = {
        'polymorphic_identity': 'friend_request'
    }


    def __init__(self, user):
        Notification.__init__(self)

        self._user = user

    def get_type(self):
        return 'FRIEND_REQUEST'

    def get_data(self):
        return {
            'user': self._user.get_public_view()
        }
