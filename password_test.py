import unittest # Importing the unittest module
import pyperclip
from password import Password # Importing the password class

class TestPassword(unittest.TestCase):

    '''
    Test class that defines test cases for the password class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
     # Items up here .......

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_password = Password("first_name","last_name","password_input") # create password object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_password.first_name,"first_name")
        self.assertEqual(self.new_password.last_name,"last_name")
        self.assertEqual(self.new_password.password_input,"password_input")

    def test_save_password(self):
        '''
        test_save_password test case to test if the password object is saved into
         the passowrd list
        '''
        self.new_password.save_password() # saving the new contact
        self.assertEqual(len(Password.password_list),1)


    
        # setup and class creation up here
    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            Password.password_list = []

       # other test cases here
    def test_save_multiple_password(self):
            '''
            test_save_multiple_password to check if we can save multiple password
            objects to our password_list
            '''
            self.new_password.save_password()
            test_password = Password("first_name","last_name","password_input") # new password
            test_password.save_password()
            self.assertEqual(len(Password.password_list),2)
    
        # More tests above
    def test_delete_password(self):
            '''
            test_delete_password to test if we can remove a password from our password list
            '''
            self.new_password.save_password()
            test_password = Password("first_name","last_name","password_input") # new password
            test_password.save_password()

            self.new_password.delete_password()# Deleting a password account object
            self.assertEqual(len(Password.password_list),1)


    def test_find_password_by_name(self):
        '''
        test to check if we can find a contact by first name and display information
        '''

        self.new_password.save_password()
        test_password = Password("first_name","last_name","password_input")
        test_password.save_password()

        found_password = Password.find_by_name("first_name")

        self.assertEqual(found_password.password_input,test_password.password_input)

    def test_password_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the password.
        '''

        self.new_password.save_password()
        test_password = Password("first_name","last_name","password_input") # new password
        test_password.save_password()

        password_exists = Password.password_exist("first_name")

        self.assertTrue(password_exists)
    
    def test_display_all_passwords(self):
        '''
        method that returns a list of all passwords saved
        '''

        self.assertEqual(Password.display_passwords(),Password.password_list)
    
    def test_copy_password(self):
        '''
        Test to confirm that we are copying a password from a found contact
        '''

        self.new_password.save_password()
        Password.copy_password("password_input")

        self.assertEqual(self.new_password.password_input,pyperclip.paste())

if __name__ == '__main__':
    unittest.main()