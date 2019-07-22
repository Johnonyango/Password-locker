import unittest # Importing the unittest module
import pyperclip
class Password:
    """
    Class that generates new instances of passwords
    """

    password_list = [] #Empty password list

    def __init__(self,first_name,last_name,password_input):
      # docstring removed for simplicity

       self.first_name = first_name
       self.last_name = last_name
       self.password_input = password_input
    
      # Init method up here
    def save_password(self):

        '''
        save_password method saves password objects into password_list
        '''

        Password.password_list.append(self)

    
    def delete_password(self):

        '''
        delete_password method deletes a saved password from the password_list
        '''

        Password.password_list.remove(self)

    @classmethod
    def find_by_name(cls,first_name):
        '''
        Method that takes in a name and returns a contact that matches that name.

        Args:
            name: first name to search for
        Returns :
            Password of person that matches the name.
        '''

        for password in cls.password_list:
            if password.first_name == first_name:
                return password
    
    @classmethod
    def password_exist(cls,first_name):
        '''
        Method that checks if a password account exists from the password list.
        Args:
            name: First name to search if it exists
        Returns :
            Boolean: True or false depending if the password account exists
        '''
        for password in cls.password_list:
            if password.first_name == first_name:
                    return True

        return False
    
    @classmethod
    def display_passwords(cls):
        '''
        method that returns the password list
        '''
        return cls.password_list


    @classmethod
    def copy_password(cls,password_input):
        password_found = Password.find_by_password(password_input)
        pyperclip.copy(password_found.password)
    
   
if __name__ == '__main__':
    unittest.main()    