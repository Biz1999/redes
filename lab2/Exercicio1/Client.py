from socket import *
serverName = 'localhost'
#cria socket TCP, porta
#remota # 12000
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

while True:
    sentence = input("Digite algo em letra minúscula: ")
    #Envia a mensagem
    sen = sentence.encode()#formata a mensagem
    clientSocket.send(sen)#chama encode para mandar 
    modifiedSentence = clientSocket.recv(1024).decode()
    print("From Server:", modifiedSentence)
    sentenceVerif = sentence.split()
    sentenceVerif = ' '.join(sentenceVerif[1:]).upper()
    if modifiedSentence != sentenceVerif:
        break

clientSocket.close()

