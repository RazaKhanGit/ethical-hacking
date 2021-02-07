#!usr/bin/python

from termcolor import colored
import hashlib

def tryOpen(wordlist):
    global pass_file
    try:
        pass_file = open(wordlist, 'r')

    except:
        print('[!!] No Such file at that Path')

pass_hash = input('[*] Enter MD5 hash value: ')
wordlist = input('[*] Enter Path to Password File: ')
tryOpen(wordlist)

for word in pass_file:
    print(colored('[-] Trying:' + word.strip('\n'), 'yellow'))
    enc_word = word.encode('utf-8')
    md5digest = hashlib.md5(enc_word.strip()).hexdigest()

    if md5digest == pass_hash:
        print(colored('[+] Password Found: '+word, 'green'))
        exit()
    
print(colored('[!!] Password not in list', 'red'))
