import unittest, sys
from datetime import date

sys.path.append('../../')
sys.path.append('../')
from core.src.Notification import Notification
from core.src.NotificationStatus import NotificationStatus

class NotificationTest(unittest.TestCase):
    # tests for the User class

    def setUp(self):
        self.notification = Notification(date.today())
    
    def test_constructor(self):
        self.assertEqual(self.notification.getDate(), date.today())
        self.assertEqual(self.notification.getStatus(), NotificationStatus.new)

if __name__ == '__main__':
    unittest.main()

