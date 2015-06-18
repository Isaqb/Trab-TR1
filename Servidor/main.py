
from Servidor import Envia
import socket
import select
import Queue
from threading import Thread
from time import sleep
from random import randint
import sys


envia = Envia()
envia.start()

def Recebe():
	print "Thread que recebe: criada"
	s = socket.socket()         # Cria um objeto de socket
	host = socket.gethostname() # Nome local da maquina
	port = 7000             	# Rezerva a porta para o programa
	s.bind((host, port))        
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
	t.stop()
	t.join()

if __name__ == "__main__":
	Recebe()