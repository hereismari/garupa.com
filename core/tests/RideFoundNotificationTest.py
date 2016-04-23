import unittest, sys

sys.path.append('../../')
sys.path.append('../')

from core.src.RideFoundNotification import RideFoundNotification
from core.src.User import User
from core.src.Ride import Ride

import datetime

class RideFoundNotificationTest(unittest.TestCase):

    def setUp(self):
        self.user1 = User(114110478, '123456789', 'User1', 'user1@gmail.com')
        self.user1.setPhone('(83)91234-56789')
        self.ride1 = Ride(self.user1, 124142342, 'HOME', 'minha rua', [], False, 3)

    def test_basic(self):
        notification = RideFoundNotification(self.ride1)
        self.assertEqual(notification.getRide(), self.ride1)

if __name__ == '__main__':
    unittest.main()
