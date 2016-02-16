#!/usr/bin/env python

try:
	fdesc = open("/var/log/messages", "r")
except:
	print("You haven't got the right permissions")
else:
	print("The file is opened")
finally:
	print("You should ensure that you have got the right permissions")

