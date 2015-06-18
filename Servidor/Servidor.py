import socket
import select
import Queue
from threading import Thread
from time import sleep
from random import randint
import sys

def FlipaBits(value):
	try:
		client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		host = value
		client.connect((host, 7000))
		print "GVT coloque seu codigo aki"

		client.send(value)
		client.shutdown(socket.SHUT_RDWR)
		client.close()
	except Exception as msg:
		print msg


class Envia(Thread):
	def __init__(self):
		super(Envia, self).__init__()
		self.running = True
		self.q = Queue.Queue()
 
	def add(self, data):
		self.q.put(data)
 
	def stop(self):
		self.running = False
 
	def run(self):
		q = self.q
		while self.running:
			try:
				# espera por 1 segundo:
				value = q.get(block=True, timeout=1)
				print value
				#FlipaBits(value)
			except Queue.Empty:
				sys.stdout.write('.')
				sys.stdout.flush()

		if not q.empty():
			print "Existem elementos na fila que nao podem ser lidos"
		while not q.empty():
			print q.get()