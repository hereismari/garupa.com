from NotificationStatus import NotificationStatus
from datetime import date

class Notification:

    def __init__(self, date=date.today(), status=NotificationStatus.new):
        self._status = status
        self._date = date
        self._message = 'Nova atividade!'

    def __str__(self):
        result = 'Notification\n'
        result += 'date: ' + str(self._date) + '\n'
        result += 'status: ' + str(self._status) + '\n'
        result += 'message: ' + str(self._message) + '\n'
        return result

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    """ Set and Get functions """

    def getMessage(self):
        return self._message

    def getDate(self):
        return self._date

    def getStatus(self):
        return self._status

    def setStatus(self, status):
        self._status = status
