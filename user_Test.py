import unittest 
from user import User
class TestUser(unittest.TestCase):


    def setUpClass(self):
        """
        Function to run before each test
        """
        self.new_user=User("Frankline-Kiplangat", "frankdux@1234")

    def tearDown(self):
        '''
        clean up after each test to prevent errors
        '''
        User.user_list = []

        #first test- initialization