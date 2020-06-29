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

    def test_save_mutliple_users(self):
        '''
        Function to check whether you can store more than one account
        '''
        self.new_user.save_user()
        test_user = User("test", "password")
        test_user.save_user()
        self.assertEqual(len(User.user_list), 2)

        #run third test to check if we can Delete the  user

    def test_delete_user(self):
        '''
        checking whether one can delete an account
        '''
        self.new_user.save_user()
        test_user = User("test", "password")
        test_user.save_user()
        self.new_user.delete_user()
        self.assertEqual(len(User.user_list), 1)

    def test_find_user(self):
        '''
        find a user with username
        '''
        self.new_user.save_user()
        test_user = User("test", "password")
        test_user.save_user()
        found_user = User.find_user("Frankline-Kiplangat")
        self.assertEqual(found_user.username, self.new_user.username)



if __name__ == '__main__':
  unittest.main()
