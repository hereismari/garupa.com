from time import mktime
from datetime import datetime

"""Classe usada como uma abstracao de uma notificacao, nao devera ser instanciada"""

class Notification(object):

    def __init__(self):
        self._seen = False
        self._date = datetime.now()

    def __str__(self):
        return '<Notification data: %s status: %s>' % (self.get_date(), self._seen)

    def __eq__(self, other):
        if isinstance(other, Notification): return False
        return abs(self.get_date() - other.get_date()).total_seconds() < 10

    """ Set and Get functions """

    def get_date(self):
        return self._date

    def set_seen(self, seen):
        self._seen = seen

    def get_time_stamp(self):
        return mktime(self._date.timetuple())

    def get_view(self):
        result = {}

        result['status'] = self._seen()
        result['data'] = self.get_data()
        result['type'] = self.get_type()
        result['date'] = int(self.get_time_stamp() * 1000)

        return result
