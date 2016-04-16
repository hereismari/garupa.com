from NotificationStatus import *
from datetime import date

class Notification:

    def __init__(self, date, status=NotificationStatus.new):
        self._status = status
        self._date = date
        self._message = "Nova notificação"

    def __str__(self):
        return self._date, self._status, self._message

    """ Set and Get functions """
    
    def getMessage(self):
        return self._message

    def getStatus(self):
        return self._status

    def setStatus(self, status):
        self._status = status

    def getDate(self):
        return self._date

    def setDate(self, date):
        return self._date = date

