#!/usr/bin/env python

import thread
from scapy.all import *

def check_ports(arg):
	address = arg.pop(0)

	for port in arg[0]:
		try:
			try:
				ans,unans = sr1(IP(dst=address)/TCP(dport=51477,flags="S"),retry=2, timeout=1, verbose=0)
				ans.summary(lfilter = lambda (s,r): r.sprintf("%TCP.flags%") == "SA",prn=lambda(s,r):r.sprintf("%TCP.sport% is open"))
			except TypeError:
				continue
		except Exception as e:
			print(str(e))


address = raw_input("Type your goal address: ")
min_port = int(raw_input("Type the left side of address interval: "))

ports = range(min_port, min_port + 100)

tab = []

i = 0
j = 0

while i < len(ports):
	tab.append(ports[i: i + 10])
	
	thread.start_new_thread(check_ports, ([address, tab[j]],))
	i += 10
	j += 1

while True:
	pass
