class Notification:

    def __init__(self, status=NEW_NOTIFICATION):
        self._status = status

    def getStatus(self):
        return self._status

    def setStatus(self, status):
        self._status = status

