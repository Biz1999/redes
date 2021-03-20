from socket import *
serverName = 'localhost'
#cria socket TCP, porta
#remota # 12000
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

print('****OPERAÇÕES ARITMÉTICAS****')
print('OPERAÇÕES ACEITAS : +, -, *, /')


while True:
    
    sentence = input("Insira os valores e a operação (1 + 1): ")
    sentence = sentence.split()
    if "+" in sentence : 
        sentence = "SOMA " +sentence[0] + " " + sentence[2]

    elif "-" in sentence:
        sentence = "SUBTRAÇÃO " +sentence[0] + " " + sentence[2]

    elif "*" in sentence:
        sentence = "MULTIPLICAÇÃO " +sentence[0] + " " + sentence[2]

    elif "/" in sentence:
        sentence = "DIVISÃO " +sentence[0] + " " + sentence[2]
    
    else:
        print("Operação não consegue ser interpretada")
        break

    print("Mensagem enviada à Calculadora:", sentence)
    sen = sentence.encode()#formata a mensagem
    clientSocket.send(sen)#chama encode para mandar  

    modifiedSentence = clientSocket.recv(1024).decode()
    print("RESPOSTA DA CALCULADORA:", modifiedSentence, "\n")

clientSocket.close()

