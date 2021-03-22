from socket import *
import getpass
serverName = 'localhost'

#cria socket TCP, porta
#remota # 12000
serverPort = 12000

#captura usuariolog
user_log = getpass.getuser()

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

#Parte que realiza o primeiro contato com o servidor, passando usuário logado
#O Servidor vai questionar se o cliente deseja ser chamado pelo login ou por outro nome

user_log = user_log.encode() #Formata o usuario logado
clientSocket.send(user_log) #Envia o usuário para o servidor

mensagemBoasVindas = clientSocket.recv(1024).decode()
print("Alex:", mensagemBoasVindas)

opcao = input("1 para manter seu nome ou digite um novo nome: ")
opcao = opcao.encode()
clientSocket.send(opcao)

#Recebe instruções de como deve ser o tratamento
mensagemBoasVindas = clientSocket.recv(1024).decode()
print("Alex:", mensagemBoasVindas)


while True:
    sentence = input("Pergunte algo à Alex: ")
    #Envia a mensagem
    sen = sentence.encode()#formata a mensagem
    clientSocket.send(sen)#chama encode para mandar 
    modifiedSentence = clientSocket.recv(1024).decode()
    print("Alex:", modifiedSentence)
    errorDetection = modifiedSentence.split()
    shutDown = ['ERRO','até', 'Até', 'logo']

    if any(i in errorDetection for i in shutDown):
        break

clientSocket.close()