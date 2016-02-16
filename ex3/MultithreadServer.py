#!/usr/bin/env python

import MultiThread
import socket
import threading

HOST = "0.0.0.0"
PORT = 54711

# create the server's socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

while True:
	s.listen(1)

	client, client_data = s.accept()

	client_thread = MultiThread.Client(client)
	client_thread.setDaemon(True)
	client_thread.start()
