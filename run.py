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
