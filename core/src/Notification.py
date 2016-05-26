from time import mktime
from datetime import datetime
from core import generator

"""Classe usada como uma abstracao de uma notificacao, nao devera ser instanciada"""

class Notification(object):

    def __init__(self):
        self._nid = generator.get_notification_id()
        self._date = datetime.now()
        self._seen = False

    def __str__(self):
        result = 'Notification\n'
        result += 'date: ' + self._date + '\n'
        result += 'status: ' + ('seen' if self._seen else 'unseen') + '\n'
        return result

    def __eq__(self, other):
        if not isinstance(other, Notification): return False
        return abs(self.getDate() - other.getDate()).total_seconds() < 10

    """ Set and Get functions """

    def getNid(self):
		return self._nid

    def getDate(self):
        return self._date

    def getReadableDate(self):
        return self._date.strftime('%d-%m-%Y')

    def getSeen(self):
        return self._seen

    def mark(self):
        self._seen = True

    def getTimestamp(self):
        return mktime(self.getDate().timetuple())

    def getView(self):
        return {
            'nid': self.getNid(),
            'data': self.getData(),
            'type': self.getType(),
            'seen': self.getSeen(),
            'timestamp': int(self.getTimestamp() * 1000)
        }
