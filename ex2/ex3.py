#!/usr/bin/env python

import sys
import os
import glob

def recursive(path):
	if os.path.isdir(path):
		for i in glob.glob(os.path.join(path, "*")):
			try:
				line = ""
				
				if os.path.isdir(i):
					line += "d"
				else:
					line +="-"

				if os.access(i, os.R_OK):
					line += "r"
				else:
					line += "-"

				if os.access(i, os.W_OK):
					line += "w"
				else:
					line += "-"

				if os.access(i, os.X_OK):
					line += "x"
				else:
					line += "-"
				
				fdesc = os.open(i, os.O_RDONLY)
				
				fstat = os.fstat(fdesc)
				uid = fstat[4]
				gid = fstat[5]
				f_size = fstat[6]
				m_time = fstat[8]
				
				line += " " + str(uid) + " " + str(gid)
				
				line += " " + str(f_size) + " " + str(m_time) + " " + i
				
				print(line + "\n")
				
				recursive(i)
				
			except:
				print("")
	else:
		return
		
if len(sys.argv) > 0:
	for item in sys.argv:
		recursive(item)
else:
	print("You didn't provide the exact data")
				
