from userCredentials import UserCredentials
from user import User
import random

# Create account
def create_useraccount(username, password):
    """
    Function to create a new account
    """
    new_user = User(username, password)
    return new_user

def save_user(user):
    """
    Function to saver user account
    """
    user.save_user()

def save_userCredentials(userCredentials):
    
    userCredentials.save_userCredentials

    #Find user

def find_user(username):

    return User.find_user(username)

def create_userCredentials(account, email, password):
    """
    Function to create user details
    """
    new_userCred= UserCredentials(account, email, password)
    return new_userCred

def save_userCred(userCred):
    """
    Method to display saved user credentials
    """
    userCred.save_userCred()

def display_userCred():
    '''
    method to display all the saved credentials
    '''
    return UserCredentials.display_userCred()

def find_account(account):

    return UserCredentials.find_account(account)

def delete_userCred(account):

    account.delete_userCred()
