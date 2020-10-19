## Task: write function to take input as (name email and phone number), another function to check if they are correct eg name field is not empty. email is in correct email format and not empty and phone number is integer and not empty, and another function to display the result
## Approach: Checked name, email, phone number one by one. Used regualar expressions to find if the given emails is correct or not. try/except for phone number and condition for name
## Solution:
'''
import re


def check(name, email, phone_number):
    if name and name != '':
        if re.search('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$', email):
            if len(phone_number) == 10:
                try:
                    phone_number = int(phone_number)
                    return True
                except:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False


def display(name, email, phone_number):
    if check(name, email, phone_number):
        print('Yes The Format Is Correct')
    else:
        print('The format is incorrect, Please try again')


def take_input():
    name = input('Enter you name: ')
    email = input('Enter your email address: ')
    phone_number = input('Enter your phone number: ')
    display(name, email, phone_number)


take_input()
'''
## Author: Sampada Regmi
