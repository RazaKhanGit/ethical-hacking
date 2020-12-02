#1/usr/bin/python

import socket
import os
import sys

def retBanner(ip, port):
	try:
		socket.setdefaulttimeout(2)
		s = socket.socket()
		s.connect((ip,port)) #connecting to the port of the IP
		banner = s.recv(1024) #recieving atmost 1024 bytes of data once we connect to the target
		return banner
	except:
		return

def chechkVulns(banner, filename):
	f = open(filename, "r")
	for line in f.readlines():
		if line.strip("\n") in banner:
			print("[+] Server is vulnerable: ", banner.strip("\n"))

def main():
	if len(sys.argv) == 2:
		filename = sys.argv[1]
		if not os.path.isfile(filename):
			print("[-] File Does Not Exist!")
			exit(0)
		if not os.access(filename, os.R_OK):
			print("[-] Access Denied!")
			exit(0)
	else:
		print("[-] Usage:", str(sys.argv[0]), "<vuln Filename>")
		exit(0)
	portlist = [21, 22, 25, 88, 110, 443, 445]
	for x in range(0, 255):
		ip = "192.168.56" + str(x)
		for port in portlist:
			banner = retBanner(ip, port)
			if banner:
				print("[+] ", ip, "/", str(port), ":", banner)
				checkVulns(banner, filename)


main()