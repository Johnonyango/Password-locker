import unittest # Importing the unittest module
from user import User # Importing the contact class
class TestUser(unittest.TestCase): 

    
    
    def setUp(self):
        '''
        method to run before each test
        '''
        self.new_user=User("John", "westend") #new User created

    def tearDown(self):
        '''
        clean up after every test
        '''
        User.user_list = []

    def test__init(self):
        '''
        checking if class has initialized as expected
        '''
        self.assertEqual(self.new_user.username, "John")
        self.assertEqual(self.new_user.password, "westend")

    def test_save_user(self):
        '''
        check whether the user information can be saved 
        in the user list
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.user_list), 1)

    def test_save_mutliple_users(self):
        '''
        check whether you can store more than one user
        '''
        self.new_user.save_user()
        test_user = User("test", "password")
        test_user.save_user()
        self.assertEqual(len(User.user_list), 2)

    def test_delete_user(self):
        '''
        check whether the user can delete their accounts
        '''
        self.new_user.save_user()
        test_user = User("test", "password")
        test_user.save_user()
        self.new_user.delete_user()
        self.assertEqual(len(User.user_list), 1)

    def test_find_user(self):
        '''
        find a user using username
        '''
        self.new_user.save_user()
        test_user = User("test", "password")
        test_user.save_user()
        found_user = User.find_user("John")
        self.assertEqual(found_user.username, self.new_user.username)

if __name__ == '__main__':
  unittest.main()