import socket
import select
import Queue
import config as cfg
from threading import Thread
from time import sleep
from random import randint
import sys

def FlipaBits(value, flip):
	if flip == 1:
		masc = '{0:032b}'.format(1431655765) #0x55555555
	elif flip == 2:
		masc = '{0:032b}'.format(2863311530) #0xAAAAAAAA
	else:
		masc = '{0:032b}'.format(randint(0, 4294967295)) #random de 0x00000000 e 0xFFFFFFFF

	if flip != 0:
		valueInt = int(value)
		valueBin = '{0:032b}'.format(valueInt)
		valueBinFlip = int(valueBin,2) ^ int(masc,2)
		print valueBinFlip
		value = valueBinFlip
	return value

def Processa(value):
	try:
		msg = value.split()
		client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		client.connect((msg[1], int(msg[2])))
		print msg[4] + " " + msg[3]
		msg[4] = FlipaBits(msg[4],int(msg[3]))
		#print msg[4]
		client.send(' '.join(str(x) for x in msg))
		client.shutdown(socket.SHUT_RDWR)
		client.close()
	except Exception as msg:
		print msg


class Envia(Thread):
	def __init__(self):
		super(Envia, self).__init__()
		self.running = True #condicao para o programa rodar
		self.q = Queue.Queue()#criacao da fila de msgs
 
	def add(self, data):
		self.q.put(data)#adiciona msgs na fila
 
	def stop(self):
		self.running = False#faz o servidor para de rodar
 
	def run(self):
		q = self.q#cria uma copia da fila
		while self.running:
			try:
				# espera por 1 segundo:
				value = q.get(block=True, timeout=1)
				Processa(value)
			except Queue.Empty:
				sys.stdout.write('.')
				sys.stdout.flush()

		if not q.empty():
			print "Existem elementos na fila que nao podem ser lidos"
		while not q.empty():
			print q.get()