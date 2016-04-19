from NotificationStatus import NotificationStatus

import os, random, string
from datetime import datetime
from time import time

class User:

    def __init__(self, name, email, phone, uid, password=None, photo=None):

        self._name = name
        self._email = email
        self._phone = phone
        self._uid = uid
        self._password = password
        self._photo = photo

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
        return self._uid == other.getUid()

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
    def getView(self, otherUser):
        
        relationship = self.getRelationship(otherUser)
        if relationship not in ['self', 'friends']: result = getPublicView()
        else: result = getPrivateView()

        result['relationship'] = relationship
        return result

    def getRelationship(self, otherUser):
        
        isfriendOf = self.isFriendOf(otherUser)
        otherIsFriendOf = othterUser.isFriendOf(self)

        result = ''
        if self == otherUser: result = 'self'
        if not isFriendOf and not otherIsFriendOf: result = 'none'
        elif isFriendOf and not otherIsFriendOf: result = 'pending'
        elif not isFriendOf and otherIsFriendOf: result = 'available'
        else: result = 'friends'
        
    def getPublicView(self):
        result = {'name' : self.getName(), 'uid' : self.getUid(), 'photo' : self.getPhoto()}
        return result

    def getPrivateView(self):
        
        result = getPublicView()
        
        result['email'] = self.getEmail()
        result['phone'] = self.getPhone()
        result['rides'] = []

        rides = self.getRides()
        for ride in rides:
            result['rides'].append({                              
                'driver' : {                                      
                    'name': '%s' % ride.getDriver().getName(),    
                    'uid' : '%s' % ride.getDriver().getUid(),     
                    'photo': '%s' % ride.getDriver().getPhoto(),  
                },                                                
                'passengers': [ {'name': passenger.getName(), 'uid' : passenger.getUid()} for passenger in passengers]})

        return result

    """ Update rides """
    def updateRides(self):
        self._rides = [ride for ride in self._rides if ride.update()]
       
    
    
