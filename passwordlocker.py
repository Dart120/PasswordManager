#! /usr/bin/env python3
"""An insecure python program"""

passwords = {'email':'101qpq101101', 'steam': 'waletinu1@', 'clubpenguin': '101101'}
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
    if len(sys.argv) < 2:
        print('Usage: python passwordlocker.py [account] [password] - copy account password')
        sys.exit()
    account = sys.argv[1]
    password = sys.argv[2]
    passwords[account]=password
    print("Account %s added to database" % account)
    sys.exit()
    
