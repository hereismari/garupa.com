import unittest, sys

sys.path.append('../../')
sys.path.append('../')

from core.src.NewFriendNotification import NewFriendNotification
from core.src.User import User

class NewFriendNotificationTest(unittest.TestCase):

    def setUp(self):
        self.user1 = User(114110478, '123456789', 'User1', 'user1@gmail.com')
        self.user1.setPhone('(83)91234-56789')

    def test_basic(self):
        notification = NewFriendNotification(self.user1)
        self.assertEqual(notification.getAssociatedUser(), self.user1)

if __name__ == '__main__':
    unittest.main()
