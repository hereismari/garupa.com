import unittest
import sys

sys.path.append('../../')
sys.path.append('../')

from core.src.User import User
from core.src.Notification import Notification
from core.src.Ride import Ride
from core.src.NotificationStatus import NotificationStatus

class UserTest(unittest.TestCase):

    def setUp(self):

        self.user1 = User('User1', 'user1@gmail.com', '(83)91234-56789', '114110478', '123456789')
        self.user2 = User('User2', 'user2@gmail.com', '(83)91234-56789', '114110478')

        self.not1 = Notification()
        self.not2 = Notification()

        self.ride1 = Ride(self.user1, 3)
        self.ride2 = Ride(self.user2, 5)

    def test_constructor(self):
        
        user = User('User', 'user@gmail.com', '(83)91234-56789', '114110478', '123456789')
        
        self.assertEqual(user.getName(), 'User')
        self.assertEqual(user.getEmail(), 'user@gmail.com')
        self.assertEqual(user.getPhone(), '(83)91234-56789')
        self.assertEqual(user.getUid(), '114110478')
        self.assertEqual(user.getPassword(), '123456789')
        
        user = User('User', 'user3@gmail.com', '(83)91234-56789', '114110478')

        self.assertTrue(user.getPassword() != None)

    def test_addFriend(self):

        self.assertEqual(0, self.user1.numberOfFriends())
        self.assertFalse(self.user1.isFriendOf(self.user2))

        self.user1.addFriend(self.user2)

        self.assertEqual(1, self.user1.numberOfFriends())
        self.assertTrue(self.user1.isFriendOf(self.user2))

        self.user1.addFriend(self.user2)

        self.assertEqual(1, self.user1.numberOfFriends())
        self.assertTrue(self.user1.isFriendOf(self.user2))

    def test_removeFriend(self):
        self.assertEqual(0, self.user1.numberOfFriends())
        self.assertFalse(self.user1.isFriendOf(self.user2))

        self.user1.addFriend(self.user2)

        self.assertEqual(1, self.user1.numberOfFriends())
        self.assertTrue(self.user1.isFriendOf(self.user2))

        self.user1.addFriend(self.user2)

        self.assertEqual(1, self.user1.numberOfFriends())
        self.assertTrue(self.user1.isFriendOf(self.user2))

    def test_addNotification(self):

        self.assertEqual(0, self.user1.numberOfNotifications())
        self.assertEqual(0, self.user1.numberOfUnseenNotifications())

        self.user1.addNotification(self.not1)

        self.assertEqual(1, self.user1.numberOfNotifications())
        self.assertEqual(1, self.user1.numberOfUnseenNotifications())

        self.user1.addNotification(self.not2)

        self.assertEqual(2, self.user1.numberOfNotifications())
        self.assertEqual(2, self.user1.numberOfUnseenNotifications())

    def test_removeNotification(self):

        self.assertEqual(0, self.user1.numberOfNotifications())
        self.assertEqual(0, self.user1.numberOfUnseenNotifications())

        self.user1.addNotification(self.not1)

        self.assertEqual(1, self.user1.numberOfNotifications())
        self.assertEqual(1, self.user1.numberOfUnseenNotifications())

        self.user1.addNotification(self.not2)

        self.assertEqual(2, self.user1.numberOfNotifications())
        self.assertEqual(2, self.user1.numberOfUnseenNotifications())

        self.user1.removeNotification(self.not1)

        self.assertEqual(1, self.user1.numberOfNotifications())
        self.assertEqual(1, self.user1.numberOfUnseenNotifications())

        self.user1.removeNotification(self.not1)

        self.assertEqual(0, self.user1.numberOfNotifications())
        self.assertEqual(0, self.user1.numberOfUnseenNotifications())

    def test_addRide(self):

        self.assertEqual(0, self.user1.numberOfRides())

        self.user1.addRide(self.ride1)

        self.assertEqual(1, self.user1.numberOfRides())

        self.user1.addRide(self.ride2)

        self.assertEqual(2, self.user1.numberOfRides())

    def test_removeRide(self):

        self.assertEqual(0, self.user1.numberOfRides())

        self.user1.addRide(self.ride1)

        self.assertEqual(1, self.user1.numberOfRides())

        self.user1.addRide(self.ride2)

        self.assertEqual(2, self.user1.numberOfRides())

        self.user1.removeRide(self.ride1)

        self.assertEqual(1, self.user1.numberOfRides())

        self.user1.removeRide(self.ride2)

        self.assertEqual(0, self.user1.numberOfRides())

if __name__ == '__main__':
    unittest.main()

