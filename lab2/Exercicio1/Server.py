#esqueleto de um servidor HTTP/1.1

from socket import *

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
		split_request = request.split()
		if split_request[0] == "GET":
			#realiza ação pertinente ao comando GET
			params = ' '.join(split_request[1:])
			print("Solicitação do tipo GET, buscando o recurso {}".format(params))
			#supondo que a solicitação foi de sucesso
			response = (params.upper()).encode()
			connectionSocket.send(response)
		else:
			#imprimo um erro no servidor
			print("Comando não pode ser interpretado por esse servidor!")
			#crio uma mensagem de erro e envio ao cliente
			response = ("ERRO! Servidor não reconhece esse comando!").encode()
			connectionSocket.send(response)
			break
			
	connectionSocket.close()
