from time import mktime
from datetime import datetime

"""Classe usada como uma abstracao de uma notificacao, nao devera ser instanciada"""

class Notification(object):

    def __init__(self, nid):
        self._seen = False
        self._nid = nid
        self._date = datetime.now()

    def __str__(self):
        result = 'Notification\n'
        result += 'date: ' + self._date + '\n'
        result += 'status: ' + ('seen' if self._seen else 'unseen') + '\n'
        result += 'message: ' + str(self._message) + '\n'
        return result

    def __eq__(self, other):
        if isinstance(other, Notification): return False
        return abs(self.getDate() - other.getDate()).total_seconds() < 10

    """ Set and Get functions """
    
    def getNid(self):
		return self._nid
	
    def getMessage(self):
        return self._message

    def getDate(self):
        return self._date

    def getReadableDate(self):
        return self._date.strftime('%d-%m-%Y')

    def getSeen(self):
        return self._seen

    def setSeen(self, seen):
        self._seen = seen

    def getTimestamp(self):
        return mktime(self.getDate().timetuple())

    def getView(self):
        return self.getData()
