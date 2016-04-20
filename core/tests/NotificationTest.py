import unittest, sys
from datetime import date

sys.path.append('../../')
sys.path.append('../')
from core.src.Notification import Notification

class NotificationTest(unittest.TestCase):

    def test_basic(self):

        notification = Notification();
        self.assertEqual(notification.getReadableDate(), str(date.today()))
        self.assertEqual(notification.getStatus(), False)

        notification.setStatus(True)
        self.assertEqual(notification.getStatus(), True)

if __name__ == '__main__':
    unittest.main()

