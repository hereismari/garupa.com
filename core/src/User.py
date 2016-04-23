import os, random, string

class User(object):

    def __init__(self, uid, passwd, name, email):

        self._name = name
        self._uid = uid
        self._email = email
        self._password = passwd

        self._photo = '/assets/img/default-profile-pic.png'
        self._phone = 'N/A'

        self._friends = set()
        self._notifications = []
        self._rides = []

    def __eq__(self, other):
        if type(other) is not User: return False
        return self._uid == other.getUid()

    def __hash__(self):
        return self._uid

    def __str__(self):
        return self._name

    def addFriend(self, friend):
        self._friends.add(friend)

    def removeFriend(self, friend):
        self._friends.remove(friend)

    def isFriendOf(self, user):
        return user in self._friends

    def numberOfFriends(self):
        return len(self._friends)

    def addNotification(self, notification):
        self._notifications.append(notification)

    def removeNotification(self, notification):
        self._notifications.remove(notification)

    def numberOfNotifications(self):
        return len(self._notifications)

    def numberOfUnseenNotifications(self):
        result = 0
        for notification in self._notifications:
            if not notification.getSeen(): result += 1
        return result

    def addRide(self, ride):
        if ride not in self._rides:
            self._rides.append(ride)

    def removeRide(self, ride):
        self._rides.remove(ride)

    def numberOfRides(self):
        return len(self._rides)

    def generatePassword(self, length=10):
        chars = string.ascii_uppercase + string.digits + string.ascii_lowercase
        random.seed = (os.urandom(1024))
        password = ''.join(random.choice(chars) for i in range(length))
        return password

    """ Set and Get functions """
    def getName(self):
        return self._name

    def setName(self, name):
        self._name = name

    def getEmail(self):
        return self._email

    def setEmail(self, email):
        self._email = email

    def getUid(self):
        return self._uid

    def getPhone(self):
        return self._phone

    def setPhone(self, phone):
        self._phone = phone

    def getPhoto(self):
        return self._photo

    def setPhoto(self, photo):
        self._photo = photo

    def getPassword(self):
        return self._password

    def setPassword(self, password):
        self._password = password

    def getFriends(self):
        return self._friends

    def getNotifications(self):
        return self._notifications

    def getRides(self):
        return self._rides

    """ getView method """
    def getView(self, other):

        relationship = self.getRelationship(other)
        if relationship not in ['self', 'friend']: result = self.getPublicView()
        else: result = self.getPrivateView()

        result['relationship'] = relationship
        return result

    def getRelationship(self, other):

        isFriendOf = self.isFriendOf(other)
        otherIsFriendOf = other.isFriendOf(self)

        if self == other: result = 'self'
        elif not isFriendOf and not otherIsFriendOf: result = 'none'
        elif isFriendOf and not otherIsFriendOf: result = 'available'
        elif not isFriendOf and otherIsFriendOf: result = 'pending'
        else: result = 'friend'

        return result

    def getPublicView(self):
        return {
            'name' : self.getName(),
            'uid' : self.getUid(),
            'photo' : self.getPhoto()
        }

    def getPrivateView(self):
        publicView = self.getPublicView()
        self.updateRides()

        return dict(publicView, **{
            'email': self.getEmail(),
            'phone': self.getPhone(),
            'rides': [r.getView() for r in self.getRides()]
        })

    """ Update rides """
    def updateRides(self):
        self._rides = [r for r in self._rides if r.update()]
