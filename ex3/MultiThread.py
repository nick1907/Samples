#!/usr/bin/env python

import threading

class Client(threading.Thread):
	def __init__(self, client_socket):
		threading.Thread.__init__(self)
		self.client_socket = client_socket

	def run(self):
		data = "*"

		while len(data):
			data = self.client_socket.recv(4096)

			if data:
				self.client_socket.sendall(data)
