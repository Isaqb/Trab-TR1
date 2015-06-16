import socket

host = '127.0.0.1' #IP DA MaQUINA ATUAL
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
    	print('Mensagem recebida: '+ recebe+" - IP: "+str(cliente[0]))

serv_socket.close() #Encerra a conexao