
class Rating:
    
    def __init__(self, avaliation, associatedUser, message=''):
        self._avaliation = 0 
        self._associatedUser = associatedUser
        self._message = message

    def getAvaliation(self):
        return self._avaliation

    def getAssociatedUser(self):
        return self._associatedUser

    def getMessage(self):
        return self._message
