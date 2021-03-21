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
	envBV = "\n Olha quem apareceu por aqui! \n  Então ", requestUser, " se você quiser que eu te chame de outro nome basta digitar abaixo, ou digite 1 para continuar com esse belissimo nome! \n"
	
	envBV = str(" ".join(envBV)).encode()
	connectionSocket.send(envBV)



	#Recebe a opcao de nome do cliente
	requestOpcao = connectionSocket.recv(1024).decode()

	if(requestOpcao!= "1"):
    		requestUser = requestOpcao

	#Envia nova mensagem para o cliente com as instruções a serem seguidas
	respBV = "\n Ok ", requestUser , "!!! De agora em diante, digite Alex antes de qualquer conversa \n"
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
    				

				if str(clientDoubt[i]).upper() in ('BOM' ,'BOA') or clientDoubt[i]=='ola' or clientDoubt[i]=='Ola' or clientDoubt[i]=='olá' or clientDoubt[i]=='Olá' :
    					
					#Cumprimento de boa tarde, bom dia ou boa noite
					horario = datetime.now()
					if 18<=horario.hour<=23:
						horario = "Boa Noite!"
					elif 0<=horario.hour<=5 or  6<=horario.hour<=12 :
						horario = "Bom Dia!"
					elif 13<=horario.hour<=17 :
						horario = "Boa Tarde!"

					response = '\n Olá!', requestUser,'!!!', horario , ' tudo bem? \n'
					response = str(" ".join(response)).encode()
					connectionSocket.send(response)
					j+=1
				elif clientDoubt[i]=='tudo' or clientDoubt[i]=='Tudo' :
					response = ('\n Ótimo! \n ').encode()
					connectionSocket.send(response)
					j+=1
				elif clientDoubt[i]=='horas' or clientDoubt[i]=='horário' or clientDoubt[i]=='horario':

					horario = datetime.now()
					if 18<=horario.hour<=23:
						horario = "\n São exatamente " + str( datetime.now().strftime('%H:%M')) + "! Boa Noite! \n  "
					elif 0<=horario.hour<=5 or 6<=horario.hour<=12 :
						horario = "\n São exatamente " + str( datetime.now().strftime('%H:%M')) + "! Bom Dia! \n  "
					elif 13<=horario.hour<=17 :
						horario = "\n São exatamente " + str( datetime.now().strftime('%H:%M')) + "! Boa Tarde! \n  "
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