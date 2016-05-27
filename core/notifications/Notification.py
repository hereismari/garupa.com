from time import mktime
from datetime import datetime, timedelta
from core import generator

class Notification(object):

    # variavel estatica
    nid_counter = 1

    def __init__(self):
        self._nid = Notification.nid_counter
        self._date = datetime.now()
        self._seen = False

        Notification.nid_counter += 1

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
