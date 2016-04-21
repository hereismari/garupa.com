from datetime import datetime

"""Classe usada como uma abstracao de uma notificacao, nao devera ser instanciada"""

class Notification:

    def __init__(self, date=datetime.now(), status=False):
        self._status = status
        self._date = date
        self._message = 'Nova atividade!'

    def __str__(self):
        result = 'Notification\n'
        result += 'date: ' + self._date + '\n'
        result += 'status: ' + ('seen' if self._status else 'unseen') + '\n'
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

    def getStatus(self):
        return self._status

    def setStatus(self, status):
        self._status = status

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
