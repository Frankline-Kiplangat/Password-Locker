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

