class User:

    user_list = []

    def __init__(self, username, email, password):
        '''
        Function to save user credentials
        '''
        self.username = username
        self.email = email
        self.password = password

    def save_user(self):
        User.user_list.append(self)


    def delete_user(self):
        '''
        delete a user account
        '''
        User.user_list.remove(self)


    @classmethod
    def search_user(cls, username):
        '''
        search username using search terms
        '''
        for user in cls.user_list:
            if user.username == username:
                return  user
