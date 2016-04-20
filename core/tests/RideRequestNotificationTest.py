import unittest, sys

sys.path.append('../../')
sys.path.append('../')

from core.src.RideRequestNotification import RideRequestNotification
from core.src.User import User
from core.src.Ride import Ride

from datetime import date

class RideRequestNotificationTest(unittest.TestCase):

    def setUp(self):
        self.user1 = User('User1', 'user1@gmail.com', '(83)91234-56789', '114110478', '123456789')
        self.user2 = User('User2', 'user2@gmail.com', '(83)91234-56789', '114110478', '123456789')
        self.ride1 = Ride(self.user1, 3)

    def test_basic(self):
        notification = RideRequestNotification(self.ride1, self.user2)
        self.assertEqual(notification.getRide(), self.ride1)
        self.assertEqual(notification.getAssociatedUser(), self.user2)
        self.assertEqual(notification.getMessage(), 'User2 quer participar da carona do dia %s.' % str(date.today()))

if __name__ == '__main__':
    unittest.main()
