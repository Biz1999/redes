#HTTP/1.1 server template
import socket
import sys
import codecs
from datetime import datetime


# data e horário
date = (f'{datetime.now():%m-%Y %H:%M}')

# codigo da página
page = f'''<!DOCTYPE HTML>\n<html> 
        <body>
            <h1>This is THE WEB PAGE</h1> 
            <br>
            Hello World!
            <br>{date}<br>
        </body>
        </html>\r\n\r\n'''

page = codecs.open("teste.html", 'r')

page404 = '''<!DOCTYPE HTML>\n<html>
        <body>
            <h1>
            ERRO 404<br>Pagina nao encontrada
            </h1>
        </body>
        </html>\r\n\r\n'''

currentTime = datetime.now()
d = currentTime.ctime()
date_array = d.split()
data_formatada = f'Date: {date_array[0]}, {d[4:]} BRT\r\n'
# Porta
serverPort = 8081

#Criando socket
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#bind na porta
serverSocket.bind(('', serverPort))

#listening
serverSocket.listen(1)

print("Server HTTP/1.1 Initialized")
print(f'Listening to port {serverPort}')

#loop para receber as requisições

while True:
    connectionSocket, addr = serverSocket.accept()
    print("Client {} connected to server".format(addr))
    
    #Recebe a requisição
    request = connectionSocket.recv(1024).decode()

    #quebrando request
    request = request.split()


    if request[0] == "GET":

        params = request[1]
        if request[1] == '/' and len(request) > 4:
            params = request[4]
        print(request)

        #assuming the request was successful
        if params == f'localhost:{serverPort}':
            response = "\nHTTP/1.1 200 OK\r\n"
        else:
            response = "\nHTTP/1.1 404\r\n"
        response += data_formatada 
        response += "Connection: Keep-Alive\r\n"
        response += "Content-Type:text/html; charset=UTF-8\r\n\r\n"
        if params == f'localhost:{serverPort}':
            response += page
        else:
            response += page404
        print(response)
        connectionSocket.send(response.encode())

    if request[0] == "POST":
        params = request[1]
        if request[1] == '/' and len(request) > 4:
            params = request[4]
        print(request)

        #assuming the request was successful
        if params == f'localhost:{serverPort}':
            response = "\nHTTP/1.1 200 OK\r\n"
        else:
            response = "\nHTTP/1.1 404\r\n"
        response += data_formatada 
        response += "Connection: Keep-Alive\r\n"
        response += "Content-Type:text/html; charset=UTF-8\r\n\r\n"
        if params == f'localhost:{serverPort}':
            response += page
        else:
            response += page404
        print(response)
        connectionSocket.send(response.encode())

