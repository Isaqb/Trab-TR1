import thread
import socket

"""def newClient():
	ip = raw_input('Digite o ip de conexao 2: ')#Le do usuario o IP do servidor com que fara a conexao	
	port = 7000 #Utilizando a porta 7000
	mensagem = "" #Variavel que vai ler a mensagem a ser enviada
	addr = ((ip,port)) #Tupla contendo os valores do IP e PORTA
	client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#Especifica os tipos. Familia do protocolo e que sera do tipo TCP.

	client_socket.connect(addr) #Conecta com o IP e PORTA que especificamos anteriormente
	while(mensagem != "QSAIR"): #Enquanto a mensagem escrita for diferente de QSAIR ele continuara fazendo o envio
		mensagem = raw_input("Digite uma mensagem para enviar ao servidor 2: ") #Le a mensagem a ser enviada
		client_socket.send(mensagem) #Envia a mensagem pro servidor
		print("Mensagem enviada")

	client_socket.close() #Encerra a conexao
try:
	thread.start_new_thread(newClient, ())
except:
	print "Error: sem novo cliente"
"""
ip = raw_input('Digite o ip de conexao 1:')#Le do usuario o IP do servidor com que fara a conexao	
port = 7000 #Utilizando a porta 7000
mensagem = "" #Variavel que vai ler a mensagem a ser enviada
addr = ((ip,port)) #Tupla contendo os valores do IP e PORTA
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#Especifica os tipos. Familia do protocolo e que sera do tipo TCP.

client_socket.connect(addr) #Conecta com o IP e PORTA que especificamos anteriormente
while(mensagem != "QSAIR"): #Enquanto a mensagem escrita for diferente de QSAIR ele continuara fazendo o envio
	mensagem = raw_input("Digite uma mensagem para enviar ao servidor 1: ") #Le a mensagem a ser enviada
	client_socket.send(mensagem) #Envia a mensagem pro servidor
	print("Mensagem enviada")

client_socket.close() #Encerra a conexao