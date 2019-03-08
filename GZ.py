#! python3
#Password Locker

PASSWORDS = {
    'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
    'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
    'luggage': '12345'
    }

import sys
if len(sys.argv) < 2:
    print('Usage: python GY.py [account] - copy account password')
    sys.exit()

import pyperclip
account = sys.argv[1]   #firs command line arg is the account name

def copy_clipboard(acc):
    if acc in PASSWORDS:
        pyperclip.copy(PASSWORDS[acc])
        print('Password of ' + acc + ' copied to clipboard')
    else:
        print('There is no account named ' + acc)

copy_clipboard(account)
