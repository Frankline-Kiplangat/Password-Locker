from userCredentials import UserCredentials
from user import User
import random

# Create account
def create_useraccount(username, email, password):
    """
    Function to create a new account
    """
    new_user = User(username, email, password)
    return new_user

def save_user(user):
    """
    Function to saver user account
    """
    user.save_user()

def save_userCredentials(userCredentials):
    
    userCredentials.save_userCredentials

def search_user(username):

    return User.search_user(username)

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

def search_account(account):

    return UserCredentials.search_account(account)

def delete_userCred(account):

    account.delete_userCred()

def main():
    print("*" * 50)
    print("Hey There! Welcome. Enter your name: ")
    name = input ()
    print(f"{name}, Sign up to continue")
    print("*" * 70)
    print ('\n')
    print("Use the short codes : 'su' to Sign Up, 'li' to Log In, 'ex' to Exit ")
    
    while True:
        short_code =input().lower()

        if short_code == 'su':
            print("Create New Account...")
            print("Key in your details: ")
            print("Username: ")
            Username = input()
            print('\n')
            print("email")
            email = input()

            print("Input password: ")
            password = input()
            
            save_user(create_useraccount(Username, email, password))
            print('\n')
            print(f"{name}  Acc Info:")
            print(f"username : {Username} , email: {email} , password: {password}")
            print('\n')
            print(f"You have successfully logged in. Welcome {Username}!")
            print ('\n')
            print ('\n')
           
            print("Use these codes: 'ca' to Create a new Account, 'da' to Display Account, 'fa' to search Account, 'gp' to Generate a Password, 'ex' to exit")
            print ('\n')

 

        elif short_code == "ca":
            print("Enter your account details: ")
            print("Account Name: ")
            account = input()
            print("Email: ")
            email = input()

            print("Do you want to generate a password")
            if input()== "yes":
                letters = "any"
                how_many= len (letters)
                print("How long would you like your password to be? ")
                print(f"p.s: Maximum length of your password is {how_many}")
                lent = int(input())
                
                password = "" .join(random.sample(letters, lent))
                print(f"Your password has {lent} characters ")
                print(password)
                
                save_userCredentials(create_userCredentials(account, email, password))
                print("UserCredentials saved! Enter 'da' to see your account")
                print ('\n')
                print ('\n')
                print ("Use the short code 'ca' to create a new account")
                print ('\n')
            elif input() == "no":
                print ("password: ")
                password = input()
                save_userCred(create_userCredentials(account, email, password))
                print ('\n')
                print("Use these short codes: 'ca' to create a new account")
                print ('\n')

                save_user(create_userCredentials(account, email, password))
                save_userCred(create_userCredentials(account, email, password))
                print('\n')
                print(f"New User {account} {email} created")
                print('\n')

            else:
                print("I did not capture that. Please use shortcode 'ca' and start again")

        elif short_code == "da":
            print(f"These are the credentials for {name}:")
            print ('\n')
            for userCred in display_userCred():
                    print(f"{userCred.account}\n {userCred.email}\n {userCred.password}")
            else: 
                print ('\n')
                print("You do not have any accounts saved")

        elif short_code == "fa":
                print("Key the name of the account you are looking for: ")
                search_userCred = input()
                if search_account(search_userCred):
                    search_acc = search_account(search_userCred)
                    print(f"{search_acc.account} {search_acc.email} {search_acc.password}")
                else: print("Account does not exist!")

        elif short_code == "gp":
                letters= "any"
                how_many = len(letters)
                print("How long would you like your password to be? ")
                print(f"p.s: Maximum length of your password is {how_many}")
                lent = int(input())
                password = "" .join(random.sample(letters, lent))
                print(f"Your password has {lent} characters ")
                print(password)

        elif short_code == "ex":
            print("logging out...")
            print ('\n')
            print("logged out")
            print ('\n')
            break
                    
        else:
            print("Invalid inputs, please  use these short codes : 'ca' to create a new account, 'da' to display accounts, 'fa' to search an account, 'de' to delete account , 'gp' to generate a random password and 'ex' t0 logout")
if __name__=='__main__':
    main()