#!/usr/bin/env python

import sys
import glob
import os

def recursive(path):
	if os.path.isdir(path):
		for i in glob.glob(os.path.join(path, "*")):
			print(i)
			recursive(i)
	else:
		return

if len(sys.argv) > 0:
	for item in sys.argv:
		recursive(item)
else:
	print("You should add arguments to this program")
