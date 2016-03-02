""" issues:
- bug in quitting from logged in user - login calls showmenu() while still in while loop; returns back to it when user quits rather than exiting while loop completely (current bandaid patch: sys.exit())

- encrypt password
"""

import time, shelve, sys
class UserDatabase:
    """ create a UserDatabase class that stores a dictionary of users as keys and their passwords and last login time
        as the corresponding values """
    def __init__(self, dbname):
        """ initializes database and immediately calls showmenu() """
        self.database = shelve.open(dbname, writeback=True)
        self.showmenu()
    def get_users(self):
        """ prints list of users and their last login time """
        print("Current Users: ")
        for user in self.database:
            print("\t" + user + "\tlast logged in: {}".format(time.ctime(self.database[user][1])))
    def newuser(self):
        """ creates a new entry into database (username : [password, last login time]) """
        prompt_name = "Please pick a username (only alphanumeric characters allowed): "
        while True:
            username = input(prompt_name)
            if username in self.database:
                prompt_name = "Username taken, please try again: "
                continue
            elif not username.isalnum():
                prompt_name = "Special characters not allowed, please try again: "
                continue
            else:
                break
        password = input("Please set your password: ")
        self.database[username] = [password, time.time()]
    def login(self):
        """ prompts user for username and password to login to database """
        username = input("Username: ")
        if username in self.database:
            password = input("Password: ")
            correct_passwd = self.database.get(username)
            if password == correct_passwd[0]:
                self.database[username][1] = time.time()
                return self.showmenu(username=username)
            else:
                print("Incorrect password")
        else:
            print("No user '{}' in the system.".format(username))
            return self.showmenu()
    def update_passwd(self, username):
        """ lets user update their password """
        verify = input("Enter old password: ")
        old_pw = self.database.get(username)
        if verify == old_pw[0]:
            new_pw = input("Enter new password: ")
            check = input("Enter new password again: ")
            if check == new_pw:
                self.database[username][0] = new_pw
                self.database.sync()
                print("Password successfully changed.")
    def deleteuser(self, username):
        """ lets user delete their account """
        verify = input("To delete account, enter password for user {}: ".format(username))
        passwd = self.database.get(username)
        if verify == passwd[0]:
            print("User {} successfully deleted.".format(username))
            del self.database[username]
            self.database.sync()
        else:
            print("Password incorrect.")
        self.showmenu(username=None)
    def showmenu(self, username=None):
        """ menu interface for not logged in user to login or create an account. if user is logged in, a different prompt menu
            is displayed to allow user to change password, display current users in database, or delete their account """
        if username:
            prompt = "\nWelcome back {}\n(A)ll Users\nChange (P)assword\n(D)elete Account\n(Q)uit\nEnter choice: ".format(username)
        else:
            prompt = "\nWelcome\n(C)reate Account\n(L)ogin\n(Q)uit\nEnter choice: "
        done = False
        while not done:
            chosen = False
            while not chosen:
                try:
                    choice = input(prompt).strip()[0].lower()
                    if username:
                        if choice not in 'apdq':
                            print ('invalid option, try again')
                        else:
                            chosen = True
                    else:
                        if choice not in 'clq':
                            print ('invalid option, try again')
                        else:
                            chosen = True
                except (EOFError, KeyboardInterrupt, IndexError):
                    choice = 'q'
                    chosen = True
                    print ('\nYou picked: [%s]' % choice)
            # if proper choice was made, call on corresponding method, or exit while loop
            if choice == 'c': self.newuser()
            if choice == 'l': self.login()
            if choice == 'p': self.update_passwd(username)
            if choice == 'a': self.get_users()
            if choice == 'd': self.deleteuser(username)
            if choice == 'q': done = True
        self.database.close()
        sys.exit()

if __name__ == '__main__':
    UserDatabase("users")
