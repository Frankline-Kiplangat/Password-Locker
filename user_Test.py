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
  
    def test__init(self):
        '''
        check if class is initialiazing as expected
        '''
        self.assertEqual(self.new_user.username, "Frankline-Kiplangat")
        self.assertEqual(self.new_user.password, "frankdux@1234")



    def test_save_user(self):
        '''
        check whether the user information can be saved 
        in the user list
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list), 1)

        #run second test to check if we can save multiple users
             