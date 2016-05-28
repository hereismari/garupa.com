from time import mktime
from datetime import datetime, timedelta
from core.database import db

class Notification(db.Model):

    _nid = db.Column('nid', db.Integer, primary_key=True)
    _owner = db.Column(db.ForeignKey('user.uid'))

    _date = db.Column(db.DateTime)
    _seen = db.Column(db.Boolean)

    _type = db.Column(db.String(30))


    __tablename__ = 'notification'

    __mapper_args__ = {
        'polymorphic_on': _type,
        'polymorphic_identity': 'base'
    }


    def __init__(self):
        self._date = datetime.now()
        self._seen = False

    def __eq__(self, other):
        if not isinstance(other, Notification): return False
        return abs(self.get_date() - other.get_date()) < timedelta(seconds=10)

    def __hash__(self):
        return self._nid

    def get_nid(self):
		return self._nid

    def get_date(self):
        return self._date

    def get_seen(self):
        return self._seen

    def set_seen(self):
        self._seen = True

    def get_timestamp(self):
        return mktime(self._date.timetuple())

    def get_view(self):
        return {
            'nid': self.get_nid(),
            'data': self.get_data(),
            'type': self.get_type(),
            'seen': self.get_seen(),
            'timestamp': int(self.get_timestamp() * 1000)
        }
