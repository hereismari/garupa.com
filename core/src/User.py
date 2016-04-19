import os, random, string

from core.src.NotificationStatus import NotificationStatus

class User:

    def __init__(self, name, email, phone, uid, password=None, profileImage=None):

        self._name = name
        self._email = email
        self._phone = phone
        self._uid = uid
        self._password = password
        self._profileImage = profileImage

        self._friends = []
        self._notifications = []
        self._rides = []

        if password == None:
            self._password = self.generatePassword()

    def addFriend(self, friend):
        if friend not in self._friends:
            self._friends.append(friend)

    def removeFriend(self, friend):
        self._friends.remove(friend)

    def isFriendOf(self, user):
        return (user in self._friends)

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
            if notification.getStatus() == NotificationStatus.new: result += 1
        return result

    def addRide(self, ride):
        if not ride in self._rides:
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

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __str__(self):
        return self._name

    """ Set and Get functions """
    def getName(self):
        return self._name

    def setName(self, name):
        self._name = name

    def getEmail(self):
        return self._email

    def setEmail(self, email):
        self._email = email

    def setEnrollment(self, uid):
        self._uid = uid

    def getEnrollment(self):
        return self._uid

    def getPhone(self):
        return self._phone

    def setPhone(self, phone):
        self._phone = phone

    def getProfileImage(self):
        return self._profileImage

    def setProfileImage(self, profileImage):
        self._profileImage = profileImage

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

