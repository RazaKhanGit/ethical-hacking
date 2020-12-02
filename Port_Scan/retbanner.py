#!/usr/bin/python

import socket

def retBanner(ip, port):
	try:
		socket.setdefaulttimeout(2)
		s = socket.socket()
		s.connect((ip,port)) #connecting to the port of the IP
		banner = s.recv(1024) #recieving atmost 1024 bytes of data once we connect to the target
		return banner
	except:
		return
	
def main():
	ports = [22, 443, 80, 23, 405, 88]
	for x in range(0, 10):
		ip = "192.168.56." + str(x)
		for port in ports:	
			banner = retBanner(ip, port)
			if banner:
				print("[+]", ip, "/", port,": ", banner)

main()
