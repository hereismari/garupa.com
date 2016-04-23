from datetime import datetime
from time import mktime

"""Classe usada como uma abstracao de uma notificacao, nao devera ser instanciada"""

class Notification:

    def __init__(self, associatedData):
        self._seen = False
        self._date = datetime.now()

    def __str__(self):
        result = 'Notification\n'
        result += 'date: ' + self._date + '\n'
        result += 'status: ' + ('seen' if self._seen else 'unseen') + '\n'
        result += 'message: ' + str(self._message) + '\n'
        return result

    def __eq__(self, other):
	if type(other) == Notification: return False
        return abs(self.getDate() - other.getDate()).total_seconds() < 10

    """ Set and Get functions """

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
    	result['data'] = self.getData()
	result['type'] = 'NOTIFICATION'
    	result['date'] = int(self.getTimestamp() * 1000)

    	return result

