#!/usr/bin/env python

import os

pid = os.fork()

if pid == 0:
	print("Jestem procesem potomnym")
	print("wspoldziele pamiec itp. z procesem rodzicem")
	print("moj pid to: %d" % os.getpid())
else:
	print("Jestem procesem rodzica")
	print("Moj pid to: %d" % os.getpid())
