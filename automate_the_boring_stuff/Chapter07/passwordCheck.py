#! python3
# passwordCheck.py - check the password that the user enter, the password should have at least eight characters long, contains both uppercase and lowercase characters, and has at least one digit.

import os, re

pwRegex = re.compile(r'''(
    ^(?=.*[A-Z])
    (?=.*[a-z])
    (?=.*\d)
    [A-Za-z0-9]{8,}$
    )''', re.VERBOSE)    

while True:
    pw = input('please input a password: ')
    if pwRegex.search(pw) is not None:
        print('the password is OK.')
        break
    else:
        print('the password is too weak, please enter another')