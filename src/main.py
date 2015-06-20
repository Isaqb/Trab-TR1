
from Servidor import Envia
import socket
import select
import Queue
import config as cfg
from threading import Thread
from time import sleep
from random import randint
import sys


envia = Envia()
envia.start()

def Recebe():
	print "Thread que recebe: criada"
	s = socket.socket()         # Cria um objeto de socket
	port = cfg.PORT            	# Rezerva a porta para o programa
	s.bind((cfg.SERVIDOR, port))        
	s.listen(10)                #Define o numero maximo de clientes para 10


	while True:
	    try:
	        client, addr = s.accept()#Conecta com o cliente
	        ready = select.select([client,],[], [],2)
	        if ready[0]:
	            data = client.recv(4096)
				#print "colocando".data."na fila" 
	            envia.add(data)
	    except KeyboardInterrupt:#Morreu com input do terminal
	        print
	        print "Pare"
	        break
	    except socket.error, msg:
	        print "Socket error! %s" % msg
	        break
	Limpar()


def Limpar():
	envia.stop()
	envia.join()

if __name__ == "__main__":
	Recebe()