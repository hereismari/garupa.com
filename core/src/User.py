class User:

    def __init__(self, profileImage, name, email, phone, enrollment, password):

        self._profileImage = profileImage
        self._name = name
        self._email = email
        self._phone = phone
        self._enrollment = enrollment
        self._password = password

        self._friends = []
        self._notifications = []
        self._rides = []

    def addFriend(self, friend):
        self._friends.append(friend)

    def removeFriend(self, friend):
        self._friends.remove(friend)

    def addNotification(self, notification):
        self._notifications.append(notification)

    def removeNotification(self, notification):
        self._notifications.remove(notification)

    def addRide(self, ride):
        self._rides.add(ride)

    def removeRide(self, ride):
        self._rides.remove(ride)

    """ Set and Get functions """
    def getName(self):
        return self._name

    def setName(self, name):
        self._name = name

    def getEmail(self):
        return self._name

    def setEmail(self, email):
        self._email = email

    def getEmail(self):
        return self._email

    def setEnrollment(self, enrollment):
        self._enrollment = enrollment

    def getEnrollment(self):
        return self._enrollment

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

