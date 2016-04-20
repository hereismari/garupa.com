import unittest, sys

sys.path.append('../../')
sys.path.append('../')

from core.src.FriendRequestNotification import FriendRequestNotification
from core.src.User import User

class FriendRequestNotificationTest(unittest.TestCase):

    def setUp(self):
        self.user1 = User('User1', 'user1@gmail.com', '(83)91234-56789', '114110478', '123456789')

    def test_basic(self):
        notification = FriendRequestNotification(self.user1)
        self.assertEqual(notification.getAssociatedUser(), self.user1)
        self.assertEqual(notification.getMessage(), 'User1 quer ser seu amigo.')

if __name__ == '__main__':
    unittest.main()
