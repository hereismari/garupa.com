from datetime import datetime
from time import mktime

"""Classe usada como uma abstracao de uma notificacao, nao devera ser instanciada"""

class Notification:

    def __init__(self, associatedData):
        self._seen = False
        self._date = datetime.now()
        self._data = associatedData
        self._message = 'Nova atividade!'

    def __str__(self):
        result = 'Notification\n'
        result += 'date: ' + self._date + '\n'
        result += 'status: ' + ('seen' if self._seen else 'unseen') + '\n'
        result += 'message: ' + str(self._message) + '\n'
        return result

    def __eq__(self, other):
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

    def getData(self):
    	return self._data

    def getTimestamp(self):
        return mktime(self.getDate().timetuple())

    def getView(self):
    	result = self.getData()
    	result['date'] = int(self.getTimestamp() * 1000)

# PARTE DE TESTES GAMBIARROSAMENTE FEITA

if __name__ == '__main__':
	d1 = datetime.now()
	not1 = Notification()
	print not1.getReadableDate()
	print not1.getDate(), d1


    # fazer passar alguns segundos
	x = 0
	while x != 10000000000:
		x += 100

	not2 = Notification()
	d2 = datetime.now()
	print not2.getReadableDate()

	print abs(not1.getDate() - not2.getDate()).total_seconds()
