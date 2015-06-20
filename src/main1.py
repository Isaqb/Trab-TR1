from threading import Thread
from Cliente1 import Cliente
import config as cfg
import socket
import sys




if __name__ == "__main__":
	i = 0
	for c in cfg.clientes:
		thread = Cliente(c,i)
		thread.start()
		i += 1
