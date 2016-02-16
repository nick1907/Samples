#!/usr/bin/env python

import threading
import Queue
from ftplib import FTP

class ThreadWorker(threading.Thread):
	def __init__(self, queue):
		threading.Thread.__init__(self)
		self.queue = queue

	def run(self):
		while True:
			print(self.queue.get())
			ftp = FTP(self.queue.get(), timeout=5)
			ftp.login()
			ftp.cwd('/')
			ftp.retrlines('LIST')
			ftp.quit()
			self.queue.task_done()

queue = Queue.Queue()

for i in range(5):
	worker = ThreadWorker(queue)
	worker.setDaemon(True)
	worker.start()

site_list = ['ftp.controlling.pl', 'ftp.cyfra.info.pl',
		'ftp.extis.com.pl', 'ftp.gust.org.pl',
		'ep09.kernel.pl', 'filez.home.net.pl',
		'ftp.adax.pl', 'ftp.agh.edu.pl',
		'ftp.cad.pl', 'ftp.control.slupsk.pl']

for site in site_list:
	queue.put(site)

queue.join()

print("All done work")
