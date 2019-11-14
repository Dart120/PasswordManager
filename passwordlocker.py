#! /usr/bin/env python3
"""An insecure python program"""

passwords = {'email':'heydudes101', 'steam': 'password', 'clubpenguin': '101101'}
import sys, pyperclip
def retrivepassword():
    if len(sys.argv) < 2:
        print('Usage: python passwordlocker.py [account] - copy account password')
        sys.exit()
    account = sys.argv[1]
    if account in passwords:
        pyperclip.copy(passwords[account])
        print('The password for account: %s Has been copied to the clipboard' % account)
        sys.exit()
    else:
        print('There is no account named: %s' % account)
        sys.exit()
def addpassword():
    if len(sys.argv) < 3:
        print('Usage: python passwordlocker.py [account] [password] - adds account to database')
        sys.exit()
    account = sys.argv[1]
    password = sys.argv[2]
    passwords[account] = password
    print("Account %s added to database" % account)
    sys.exit()

def removepassword():
    if len(sys.argv) < 3:
        print('Usage: python passwordlocker.py [account] [password] - removes account from database')
        sys.exit()
    account = sys.argv[1]
    password = sys.arv[2]
    for k, v in passwords.items():
        if passwords.has_key(k) and v in passwords.values():
            del passwords[k]
            print("Account %s removed from database" % account)
            
    



    
