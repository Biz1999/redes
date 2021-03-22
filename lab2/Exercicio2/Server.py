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


connectionSocket, addr = serverSocket.accept()
print("Cliente {} conectado ao servidor".format(addr))

#loop principal que recebe as solicitações dos clientes
while True:
	#recebe solicitação vinda do cliente
	try:
		request = connectionSocket.recv(1024).decode()
			
		#quebra cada palavra da requisição
		clientDoubt = request.split()
		#Separa os numero para a operaçao
		primeiroNumero = float(clientDoubt[1]) if "." in clientDoubt[1] else int(clientDoubt[1])
		segundoNumero = float(clientDoubt[2]) if "." in clientDoubt[2] else int(clientDoubt[2])
		print("Operação desejada: %s entre %s e %s"%(clientDoubt[0],str(primeiroNumero),str(segundoNumero)))

		#Seleciona a operação para a operação
		if clientDoubt[0] == "SOMA":
			response = (str(primeiroNumero + segundoNumero)).encode()
			print("Valor:",response)

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
		
	#envia ao usuário a resposta
	connectionSocket.send(response)
			
connectionSocket.close()

