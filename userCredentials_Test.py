import unittest
from userCredentials import UserCredentials
import pyperclip

class TestUserCredentials(unittest.TestCase):
    
    def setUp(self):
        """
        Test class that defines test cases for userCredentials

        Args
            TestCase that helps in creating tests.
        """
        self.new_userCred = UserCredentials("Git", "kipfrankline@gmail.com", "Frankline-Kiplangat""frankdux@1234")
    def tearDown(self):

        UserCredentials.userCred_list =[]

        #check initialization

    def test_init(self):
        """
        test_init test case to test if object initialization has been done corectly
        """
        self.assertEqual(self.new_userCred.account, "Git") 
        self.assertEqual(self.new_userCred.email, "kipfrankline@gmail.com")
        self.assertEqual(self.new_userCred.password, "frankdux@1234")

    def test_save_userCredentials(self):
        """
        case to test if object is saved in the userCredentials list
        """
        self.new_userCred.save_userCred()
        self.assertEqual(len(UserCredentials.userCred_list),1)


def test_saving_multiple_userCreds(self):
    """
    test to check if we can save multiple user credentials to our list
    """
    self.new_userCred.save_userCred()
    test_userCred = UserCredentials ("Facebook", "user", "password")
    test_userCred.save_userCred()
    self.assertEqual(len(UserCredentials.userCred_list),2)

    # deleting userCredentials

def test_delete_userCredentials(self):
    """
    case to test if we can delete userCredentials
    """
    self.new_userCred.save_userCred()
    test_userCred = UserCredentials ("Facebook", "user", "password")
    test_userCred.save_userCred()
    self.new_userCred.delete_userCred()
    self.assertEqual(len(UserCredentials.userCred_list), 1)


    # searching userCredentials
def test_search_for_userCred(self):
    """
    case to test if we can search for credentials
    """
    self.new_userCred.save_userCred()
    test_userCred = UserCredentials ("Facebook", "user", "password")
    test_userCred.save_userCred()
    search_userCred = UserCredentials.search_account("Facebook")
    self.assertEqual(search_userCred.account, test_userCred.account)

    # test to check if account exist
  
  
def test_confirm_userCred_exists(self):
    """
    test to check if we can return a Boolean if we cannot search the account
    """

    self.new_userCred.save_userCred()
    test_userCred = UserCredentials ("Facebook", "user", "password")
    test_userCred.save_userCred()
    userCred_exists = UserCredentials.userCred_exists("Facebook")
    self.asserTrue(userCred_exists)


    # Display all credentials


def test_display_userCredentials(self):
    """
    returns a list of all credentials saved
    """
    self.assertEqual(UserCredentials.display_userCred(), UserCredentials.userCred_list)



    # copy UserCredentials

def test_copy_password(self):
    """
    case to test if the generated password can be copied to clipborad
    """
    self.new_userCred.save_userCred()
    UserCredentials.copy_password("frankdux@1234")
    self.assertEqual(self.new_userCred.password, pyperclip.paste())
  