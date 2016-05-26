import unittest, sys
import datetime

sys.path.append('../../')
sys.path.append('../')
from core.src.Notification import Notification

class NotificationTest(unittest.TestCase):

    def test_basic(self):

        notification = Notification();
        self.assertEqual(notification.getReadableDate(), datetime.datetime.now().strftime('%d-%m-%Y'))
        self.assertEqual(notification.getSeen(), False)

        notification.setSeen(True)
        self.assertEqual(notification.getSeen(), True)



if __name__ == '__main__':
    unittest.main()
