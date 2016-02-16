#!/usr/bin/env python

import socket

HOST = "0.0.0.0"
PORT = 54711

# connects to the HOST:PORT
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))

# enables reusing address
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# waits for client
s.listen(1)

client, client_data = s.accept()
data = "*"

while len(data):
	data = client.recv(4096)
	
	if data:
		client.sendall(data)

client.close()
