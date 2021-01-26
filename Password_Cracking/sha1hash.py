#!usr/bin/python

from urllib.request import urlopen
import hashlib
from termcolor import colored

sha1hash = input('[*] Enter SHA1 hash: ')

passlist = str(urlopen('https://raw.githubusercontent.com/iryndin/10K-Most-Popular-Passwords/master/passwords.txt').read(), 'utf-8')

for password in passlist.split('\n'):
    hashguess = hashlib.sha1(bytes(password, 'utf-8')).hexdigest()
    if hashguess == sha1hash:
        print(colored('[+] The password is '+str(password), 'green'))
        quit()

print(colored('Password not in password list', 'red'))