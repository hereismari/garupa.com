from core.notifications import Notification
from core.database import db

class FriendAccepted(Notification):

    _nid = db.Column('nid', db.Integer, db.ForeignKey('notification.nid'), primary_key=True)

    _user = db.relationship('User')
    _user_id = db.Column(db.ForeignKey('user.uid'))


    __tablename__ = 'notification$friend_accepted'

    __mapper_args__ = {
        'polymorphic_identity': 'friend_accepted'
    }


    def __init__(self, user):
        Notification.__init__(self)

        self._user = user

    def get_type(self):
        return 'NEW_FRIEND'

    def get_data(self):
        return {
            'user': self._user.get_public_view()
        }
