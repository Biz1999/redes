#esqueleto de um servidor HTTP/1.1

from socket import *
from datetime import *

#define qual o so   cket irá escutar
serverPort = 12000

#cria o socket
serverSocket = socket(AF_INET, SOCK_STREAM)

#atribuir o socket a uma porta especifica
serverSocket.bind(("", serverPort))

#inicia o "listening"
serverSocket.listen(1)

print("Servidor HTTP/1.1 Inicializado")



#loop principal que recebe as solicitações dos clientes
while True:
	connectionSocket, addr = serverSocket.accept()
	print("Cliente {} conectado ao servidor".format(addr))
	while True:
		#recebe solicitação vinda do cliente
		request = connectionSocket.recv(1024).decode()
		#quebra cada palavra da requisição
		clientDoubt = request.split()
		if clientDoubt[0] == "Alex":
			j=0
			for i in range(1,len(clientDoubt)):
				if clientDoubt[i]=='ola' or clientDoubt[i]=='Ola' or clientDoubt[i]=='olá' or clientDoubt[i]=='Olá' :
					response = ('Olá! Tudo bem?').encode()
					connectionSocket.send(response)
					j+=1
				elif clientDoubt[i]=='tudo' or clientDoubt[i]=='Tudo' :
					response = ('Ótimo!').encode()
					connectionSocket.send(response)
					j+=1
				elif clientDoubt[i]=='horas' or clientDoubt[i]=='horário' or clientDoubt[i]=='horario':
					horario = "São exatamente " + str( datetime.now().strftime('%H:%M'))
					response = ( horario ).encode()
					connectionSocket.send(response)
					j+=1
			
			if j==0:
				print("Comando não pode ser interpretado por esse servidor!")
				#crio uma mensagem de erro e envio ao cliente
				response = ("ERRO ! Alex não reconhece esse comando! Abra nova conexão").encode()
				connectionSocket.send(response)
				break
		else:
			#imprimo um erro no servidor
			print("Comando não pode ser interpretado por esse servidor!")
			#crio uma mensagem de erro e envio ao cliente
			response = ("ERRO ! Alex não reconhece esse comando! Abra nova conexão").encode()
			connectionSocket.send(response)
			break
			
	connectionSocket.close()
