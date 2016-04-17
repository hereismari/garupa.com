import unittest
import sys

sys.path.append('../../')
sys.path.append('../')
from core.src.User import User

class UserTest(unittest.TestCase):
    # tests for the User class

    def setUp(self):
        user1 = User('User1', 'user1@gmail.com', '(83)91234-56789', '114110478', '123456789')
    
    
    def test_constructor(self):
        
        user2 = User('User2', 'user2@gmail.com', '(83)91234-56789', '114110478', '123456789')
        
        self.assertEqual(user2.getName(), 'User2')
        self.assertEqual(user2.getEmail(), 'user2@gmail.com')
        self.assertEqual(user2.getPhone(), '(83)91234-56789')
        self.assertEqual(user2.getEnrollment(), '114110478')
        self.assertEqual(user2.getPassword(), '123456789')
        
        user3 = User('User3', 'user3@gmail.com', '(83)91234-56789', '114110478')

        self.assertTrue(user3.getPassword() != None)

if __name__ == '__main__':
    unittest.main()

