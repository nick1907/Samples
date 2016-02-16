#!/usr/bin/env python

import threading
import random

class ThreadWorker(threading.Thread):
	def __init__(self, variable, lock):
		threading.Thread.__init__(self)
		self.variable = variable
		self.lock = lock

	def run(self):
		for i in range(5):
			self.lock.acquire()
			variable = random.randint(1,100)
			print(variable)
			self.lock.release()

lock = threading.Lock()
variable = 0

# creates threads
t1 = ThreadWorker(variable, lock)
t2 = ThreadWorker(variable, lock)
t3 = ThreadWorker(variable, lock)

# sets threads
t1.setDaemon(True)
t2.setDaemon(True)
t3.setDaemon(True)

# starts thread
t1.start()
t2.start()
t3.start()

x = raw_input()
