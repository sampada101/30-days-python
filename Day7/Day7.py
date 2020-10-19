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
