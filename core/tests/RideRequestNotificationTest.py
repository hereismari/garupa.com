import unittest, sys

sys.path.append('../../')
sys.path.append('../')

from core.src.RideRequestNotification import RideRequestNotification
from core.src.User import User
from core.src.Ride import Ride

import datetime

class RideRequestNotificationTest(unittest.TestCase):

    def setUp(self):
        self.user1 = User(114110478, '123456789', 'User1', 'user1@gmail.com')
        self.user1.setPhone('(83)91234-56789')
        self.user2 = User(114110478, '123456789', 'User2', 'user2@gmail.com')
        self.user2.setPhone('(83)91234-56789')
        self.ride1 = Ride(self.user1, 124142342, 'HOME', 'minha rua', [], False, 3)

    def test_basic(self):
        notification = RideRequestNotification(self.ride1, self.user2)
        self.assertEqual(notification.getRide(), self.ride1)
        self.assertEqual(notification.getAssociatedUser(), self.user2)

if __name__ == '__main__':
    unittest.main()
