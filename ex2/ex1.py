#!/usr/bin/env python

fdesc = open("/var/log/messages", "r")

for line in fdesc.readlines():
	if line.find("USB") > -1:
		print(line)
	elif line.find("usb") > -1:
		print(line)

print("End of reading")
