#!/usr/bin/env python

import thread

def print_thread_id(id):
	for i in range(5):
		print("watek o id: %d wykonal swoja prace" % id)


thread_id = range(5)

for i in range(5):
	thread.start_new_thread(print_thread_id, tuple([thread_id[i],]))


print("wywolalem watki\n")

x = raw_input()
