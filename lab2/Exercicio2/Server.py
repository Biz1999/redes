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
		try:
			request = connectionSocket.recv(1024).decode()
			#quebra cada palavra da requisição
			clientDoubt = request.split()
			primeiroNumero = int(clientDoubt[1])
			segundoNumero = int(clientDoubt[2])
			if clientDoubt[0] == "SOMA":
				response = (str(primeiroNumero + segundoNumero)).encode()

			elif clientDoubt[0] == "SUBTRAÇÃO":
				response = (str(primeiroNumero - segundoNumero)).encode()

			elif clientDoubt[0] == "MULTIPLICAÇÃO":
				response = (str(primeiroNumero * segundoNumero)).encode()
				
			elif clientDoubt[0] == "DIVISÃO":
				response = (str(primeiroNumero / segundoNumero)).encode()
				
			else:
				#imprimo um erro no servidor
				print("Comando não pode ser interpretado por esse servidor!")
				break
		except:
			break

		connectionSocket.send(response)
			
	connectionSocket.close()
