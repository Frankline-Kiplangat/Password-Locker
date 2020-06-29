import pyperclip
class UserCredentials:
    """
    class that creates instance of user accounts
    """
    userCred_list = []

    # credential list

    def __init__(self, account, email, password):

        self.account = account
        self.email = email
        self.password = password


        # saving credentials
    
    def save_userCred(self):
        """
        credentials list
        """
        UserCredentials.userCred_list.append(self)

        # deleting credentials

    def delete_userCred(self):
        """
        delete  user credentials
        """
        UserCredentials.userCred_list.remove(self)

        # searching for credentials

    @classmethod
    def find_account(cls, account):
        """
        search for accounts
        """
        for userCred in cls.userCred_list:
            if userCred.account == account:
                return userCred

        # confirming details

    @classmethod
    def userCred_exists(cls, account):
        """
        confirm if a class exits
        """
        for userCred in cls.userCred_list:
            if userCred.account == account:
                return True
            return False
    
    #Display user Credentials

    @classmethod
    def display_userCred(cls):
        """
        Function that returns all credentials
        """
        return cls.userCred_list

    @classmethod
    def copy_password(cls, password):
            find_account = UserCredentials.find_account(password)
            pyperclip.copy(find_account.password)

