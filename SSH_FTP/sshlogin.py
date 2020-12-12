#!/usr/bin/python

import wexpect # for window use wexpect, for linux use pexpect
PROMPT = ['# ', '>>> ', '> ', '\$ ']

def send_command(child, command):
    child.sendline(command)
    child.expect(PROMPT)
    print(child.before)


def connect(user, host, password):
    ssh_newkey = 'Are you sure you want to continue connecting'
    connStr = 'ssh ' + user + '@' + host
    child  = wexpect.spawn(connStr)
    print(child)
    ret = child.expect([wexpect.TIMEOUT, ssh_newkey, '[P|p]assword: '])
    if ret == 0:
        print('[-] Error Connecting')
        # return
    if ret == 1:
        child.send('yes')
        ret = child.expect([wexpect.TIMEOUT, '[P|p]assword: '])
        if ret == 0:
            print('[-] Error Connecting')
            # return
    child.sendline(password)
    child.expect(PROMPT)
    return child


def main():
    host = input("Enter the Host to Target: ")
    user = input("Enter SSH username: ")
    password = input("Enter SSH password: ")
    child = connect(user, host, password)
    send_command(child, 'ls;ps')

main()