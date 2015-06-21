import threading
import socket
import sys
import config as cfg
from md5 import Checamd5
from sha1 import Checasha1
payload = 0

class Recebe(threading.Thread):
	def __init__ (self, ip,port):
		print ("Cliente ip:"+ip+ " Cliente Port"+str(port))
		threading.Thread.__init__(self)
		self.ip = ip
		self.port = port
	def run(self):
		addr = (self.ip, self.port) #VARIAVEL CONTENDO OS VALORES DO IP E PORTA
		serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Especificamos os tipos: AF_INET que declara a familia do protocolo; SOCKET_STREAM, indica que sera TCP/IP. 
		serv_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #Essa linha serve para zerar o TIME_WAIT do Socket
		serv_socket.bind(addr) #Define para qual IP e porta o servidor deve aguardar a conexao, que no nosso caso e qualquer IP, por isso o Host e ' '. 
		serv_socket.listen(1) #Define o limite de conexoes.
		while 1: #Enquanto a mensagem recebida for diferente de QSAIR o programa continuara recebendo mensagens.
			con, servidor = serv_socket.accept() #Tupla contendo dois valores, numero da conexao e endereco IP do servidor.
			recebe = con.recv(1024) #Aguarda um dado enviado pela rede de ate 1024 Bytes
			#inicio md5:
			msg = recebe.split()
			if msg[3]=="MD5":
				md5recebida = msgrecebida(msg[5])
				if msg[5] == msg[6]:
					print "MD5: Mensagem recebida com sucesso"
				else:
					print "MD5:Mensagem com erro na flipagem:"+msg[4]	
			#fim md5
			#inicio sha1:
			if msg[3]=="SHA1":
				sha1recebida = msgrecebe(msg[5])
				if msg[5] == msg[6]:
					print "SHA1: Mensagem recebida com sucesso"
				else:
					print "SHA1:Mensagem com erro na flipagem:"+msg[4]
			#fim sha1
			print(self.ip+':Mensagem recebida: '+ recebe+" - IP: "+str(servidor[0]))

		serv_socket.close() #Encerra a conexao 



class Cliente(threading.Thread):
	def __init__ (self, ip,num):
		print ("Cliente ip:"+ip)
		threading.Thread.__init__(self)
		self.src = ip
		self.num = num
		self.lock = threading.Lock()
	def run(self):
		
		thread = Recebe(self.src,cfg.ports[self.num])
		thread.start()

		try:
			i = 0
			for ip in cfg.clientes:	       
				server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#Especifica os tipos. Familia do protocolo e que sera do tipo TCP.
				server.connect((cfg.SERVIDOR, cfg.PORT))#conecta com o servidor utilizando o ip e a porta
				#md5 inicio:
				md5enviada = msgenviada(i)
				#md5 final
				#sha1 inicio:
				sha1enviada = msgenvio(i)
				#sha1 fim
				server.send(self.src+" "+ip+" "+str(cfg.ports[i])+" "+ "MD5"+" "+str(self.num)+" "+str(i)+" "+str(md5enviada))#envia mensagem
				server.shutdown(socket.SHUT_RDWR)#encerra o socket
				server.close()#fecha coneccao
				i+=1
		except Exception as msg:
			print msg#em caso de erro, imprime msg de erro
