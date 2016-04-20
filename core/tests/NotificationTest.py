import unittest, sys
from datetime import date

sys.path.append('../../')
sys.path.append('../')
from core.src.Notification import Notification
from core.src.NotificationStatus import NotificationStatus

class NotificationTest(unittest.TestCase):

    def test_basic(self):

        notification = Notification();
        self.assertEqual(notification.getReadableDate(), str(date.today()))
        self.assertEqual(notification.getStatus(), NotificationStatus.new)

        notification.setStatus(NotificationStatus.seen)
        self.assertEqual(notification.getStatus(), NotificationStatus.seen)

if __name__ == '__main__':
    unittest.main()

