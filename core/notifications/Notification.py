from time import mktime
from datetime import datetime, timedelta
from core.database import db
from core import generator

class Notification(db.Model):

    _nid = db.Column('nid', db.Integer, primary_key=True)
    
    _date = db.Column('date', db.DateTime)
    _seen = db.Column('seen', db.Boolean)

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
