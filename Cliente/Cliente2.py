from threading import Thread 
import socket
import sys


class Envia(Thread):

	def __init__ (self, num, host_address, name):
		print ("Thread que envia: criada")
		Thread.__init__(self)
	def run(self):
		ip = '127.0.0.1'#Le do usuario o IP do servidor com que fara a conexao	
		port = 7000 #Utilizando a porta 7000
		mensagem = "" #Variavel que vai ler a mensagem a ser enviada
		addr = ((ip,port)) #Tupla contendo os valores do IP e PORTA
		client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#Especifica os tipos. Familia do protocolo e que sera do tipo TCP.

		client_socket.connect(addr) #Conecta com o IP e PORTA que especificamos anteriormente

		mensagem = '127.0.0.2' #Le a mensagem a ser enviada
		client_socket.send(mensagem) #Envia a mensagem pro servidor
		print("Mensagem enviada")

		client_socket.close() #Encerra a conexao


class Recebe(Thread):
	
	def __init__ (self, num):
		print ("Thread que recebe: criada")
		Thread.__init__(self)
	
	def run(self):
		host = '127.0.0.3' #IP DA MaQUINA ATUAL
		port = 7000 #PORTA QUE SERa UTILIZADA PARA CONEXaO
		recebe = "" #Variavel que recebera a mensagem
		addr = (host, port) #VARIAVEL CONTENDO OS VALORES DO IP E PORTA
		serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Especificamos os tipos: AF_INET que declara a familia do protocolo; SOCKET_STREAM, indica que sera TCP/IP. 
		serv_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #Essa linha serve para zerar o TIME_WAIT do Socket
		serv_socket.bind(addr) #Define para qual IP e porta o servidor deve aguardar a conexao, que no nosso caso e qualquer IP, por isso o Host e ' '. 
		serv_socket.listen(10) #Define o limite de conexoes. 

		print('Aguardando conexao...')
		con, cliente = serv_socket.accept() #Tupla contendo dois valores, numero da conexao e endereco IP do cliente.
		print('Conectado')
		print('aguardando mensagem')
		while(recebe != "QSAIR"): #Enquanto a mensagem recebida for diferente de QSAIR o programa continuara recebendo mensagens.
		    recebe = con.recv(1024) #Aguarda um dado enviado pela rede de ate 1024 Bytes
		    print('Mensagem recebida: '+recebe+" - IP: "+str(cliente[0]))
		    print('Mensagem recebida: '+recebe+" - IP: "+str(cliente[1]))

		serv_socket.close() #Encerra a conexao"""

