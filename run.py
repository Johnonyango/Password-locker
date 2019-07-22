# !/usr/bin/env python3.6
from password import Password
from user import User
def create_password(fname,lname,password_input):
   '''
   Function to create a new password
   '''
   new_password = Password(fname,lname,password_input)
   return new_password

def save_password(password):
   '''
   Function to save password
   '''
   password.save_password()

def delete_password(password):
   '''
   Function to delete a password
   '''
   password.delete_password()


def check_existing_password(first_name):
   '''
   Function that check if a password exists with that name and return a Boolean
   '''
   return Password.password_exist(first_name)
def display_password():
   '''
   Function that returns all the saved password
   '''
   return Password.display_passwords()



    #*****SIGNING IN TO THE ACCOUNT*****
def main():
   print("Hi welcome to your Password account. What is your name?")
   user_name = input()

   print(f"Hi {user_name}. What would you like to do?")

   print('\n')

   while True:
       print("Use the following short codes to : cc - create a new account,dl- delete password, disp - display accounts, ex -exit the password acount list ")

       short_code = input().lower()

#*****CC-CREATING ACCOUNT*****
       if short_code == 'cc':
           print("New Account")
           print("-"*10)

           print ("First name ....")
           f_name = input()

           print("Last name ...")
           l_name = input()


           print("Password")
           password_input = input()


           save_password(create_password(f_name,l_name,password_input))
           print ('\n')
           print(f"New Account {f_name} {l_name} {password_input} created")
           print ('\n')

       
        #*****DISPLAY ACCOUNT****
       elif short_code == 'disp':

           if display_password():
               print("Here is the list of your passwords with respective user names")
               print('\n')

               for password in display_password():
                   print(f"{password.first_name} {password.last_name} ..... {password.password_input}")

               print('\n')
           else:
               print('\n')
               print("You dont have any credentials saved yet")
               print('\n')

                #*****DELETE PASSWORD*****
        
       elif short_code == 'dl':
           print("Enter the name,password you want to delete")

           print("Delete Account")
           print("-"*10)

           print ("First name ....")
           f_name = input()

           print("Last name ...")
           l_name = input()


           print("Password")
           password_input = input()


           delete_password(password)
           print ('\n')
           print(f"Account for password: {password_input} deleted !!!")
           print ('\n')
        
        
        #*****EXIT ACCOUNT*****
       elif short_code == "ex":
           print("You have logged out.Thanks for your time,GOOD BYE! .......")
           break
       else:
           print("This server says: Please use the short codes provided to navigate")

if __name__ == '__main__':

   main()