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

	#recebe solicitação vinda do cliente
	requestUser = connectionSocket.recv(1024).decode()

	#mensagem de boas vsindas para o cliente
	envBV = "Olha quem apareceu por aqui! Então ", requestUser, " se você quiser que eu te chame de outro nome basta digitar abaixo, ou digite 1 para continuar com esse belissimo nome!"
	
	envBV = str(" ".join(envBV)).encode()
	connectionSocket.send(envBV)



	#Recebe a opcao de nome do cliente
	requestOpcao = connectionSocket.recv(1024).decode()

	if(requestOpcao!= "1"):
    		requestUser = requestOpcao

	#Envia nova mensagem para o cliente com as instruções a serem seguidas
	respBV = "Ok ", requestUser , "!!! De agora em diante, digite Alex antes de qualquer conversa"
	respBV = str(" ".join(respBV)).encode()
	connectionSocket.send(respBV)

	while True:
		#recebe solicitação vinda do cliente
		request = connectionSocket.recv(1024).decode()
		#quebra cada palavra da requisição
		clientDoubt = request.split()
		if clientDoubt[0] == "Alex":
			j=0
			for i in range(1,len(clientDoubt)):
				if clientDoubt[i]=='ola' or clientDoubt[i]=='Ola' or clientDoubt[i]=='olá' or clientDoubt[i]=='Olá' :
					response = 'Olá!', requestUser,' Tudo bem?'
					response = str(" ".join(response)).encode()
					connectionSocket.send(response)
					j+=1
				elif clientDoubt[i]=='tudo' or clientDoubt[i]=='Tudo' :
					response = ('Ótimo!').encode()
					connectionSocket.send(response)
					j+=1
				elif clientDoubt[i]=='horas' or clientDoubt[i]=='horário' or clientDoubt[i]=='horario':

					horario = datetime.now()
					if 0<=horario.hour<=5 or 18<=horario.hour<=23:
						horario = "São exatamente " + str( datetime.now().strftime('%H:%M')) + "! Boa Noite!"
					elif 6<=horario.hour<=12 :
						horario = "São exatamente " + str( datetime.now().strftime('%H:%M')) + "! Bom Dia!"
					elif 13<=horario.hour<=17 :
						horario = "São exatamente " + str( datetime.now().strftime('%H:%M')) + "! Boa Tarde!"
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
