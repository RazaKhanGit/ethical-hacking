#!/usr/bin/python
import os
os.system('color')
import socket
from termcolor import colored

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.setdefaulttimeout(2)
host = input('[*] Enter the host to scan: ')

def portscanner(port):
	if sock.connect_ex((host, port)):
		print(colored("[!!]Port %d is closed" % (port), 'red'))
	else:
		print(colored("[+]Port %d is open" % (port), 'green'))
for port in range(1, 1000):
	portscanner(port)
