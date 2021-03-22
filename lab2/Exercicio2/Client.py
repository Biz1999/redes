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

    #Determina qual operação será realizada com oque o cliente inseriu
    if "+" in sentence : 
        sentence = "SOMA " +sentence[0] + " " + sentence[2]

    elif "-" in sentence:
        sentence = "SUBTRAÇÃO " +sentence[0] + " " + sentence[2]

    elif "*" in sentence:
        sentence = "MULTIPLICAÇÃO " +sentence[0] + " " + sentence[2]

    elif "/" in sentence:
        sentence = "DIVISÃO " +sentence[0] + " " + sentence[2]
    
    #Caso não seja uma operação válida encerra o cliente
    else:
        print("Operação não consegue ser interpretada")
        break

    #formata a mensagem
    print("Mensagem enviada à Calculadora:", sentence)
    sen = sentence.encode()#chama encode para mandar  
    clientSocket.send(sen)

    modifiedSentence = clientSocket.recv(1024).decode()
    print("RESPOSTA DA CALCULADORA:", modifiedSentence, "\n")

clientSocket.close()