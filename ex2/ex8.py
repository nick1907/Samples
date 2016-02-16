#!/usr/bin/env python
import socket
import sys
import signal
import os
import threading

def signal_handler(signum, frm):
	print("You cannot kill me;) I am immortal.")

def connect(time_limit):
	IP = "127.0.0.1"
	port = 54712

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
	
	s.bind((IP, port))
	
	print("I am listening on port: %d" % port)
	
	s.listen(5)
	
	data = "*"
	
	while True:
		try:
			conn, addr = s.accept()
		
			data = conn.recv(1024)
			
			number1 = ""
			number2 = ""
			operator = ""
			
			message = ""
			
			i = 0
			recent = 0
			
			while i < len(data):
				if data[i].isdigit():
					if recent == 0:
						number1 += data[i]
					elif recent == 2:
						number2 += data[i]
					else:
						message = "Error"
						break
				
				if data[i] == "-" or data[i] == "*" or data[i] == "/"\
					or data[i] == "+" or data[i] == "%":
					operator = data[i]
					recent = 2
					
				i += 1
			
			number1 = int(number1)
			number2 = int(number2)
			
			# perform calculation
			if operator == "+":
				message = str(number1 + number2)
			elif operator == "-":
				message = str(number1 - number2)
			elif operator == "*":
				message = str(number1 * number2)
			elif operator == "/":
				message = str(number1 / number2)
			elif operator == "%":
				message = str(number1 % number2)
				
			print("server received: ")
			print(data)
			
			if not data:
				break
			conn.sendall(message)
			
			conn.close()
			
		except socket.error:
			pass
	s.close()

args = sys.argv

param = False

# kill program after provided time
def exit_after():
	os._exit(0)

for i in range(1, len(args)):
	if param and args[i].isdigit():
		t = threading.Timer(int(args[i]), exit_after)
		t.start()

		signal.signal(signal.SIGCHLD, signal_handler)
		signal.signal(signal.SIGQUIT, signal_handler)
		signal.signal(signal.SIGINT, signal_handler)
		
		connect(int(args[i]))
		t.cancel()
	elif args[i].find("-s") > -1:
		param = True

while True:
	pass
		
