from socket import *
serverName = 'localhost'
#cria socket TCP, porta
#remota # 12000
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

while True:
    sentence = input("Pergunte algo à Alex: ")
    #Envia a mensagem
    sen = sentence.encode()#formata a mensagem
    clientSocket.send(sen)#chama encode para mandar 
    modifiedSentence = clientSocket.recv(1024).decode()
    print("Alex:", modifiedSentence)
    errorDetection = modifiedSentence.split()
    j = True if "ERRO" in errorDetection else False
    if j != False:
        break

clientSocket.close()

