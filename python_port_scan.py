#! /usr/bin/python
# a simple port scnanner in python

import socket
ip = input("Enter the IP address: ")
port = input("Enter the port number: ")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if sock.connect_ex((ip,int(port))):
		print("Port", port, "is closed")
else:
		print("Port", port, "is open")
