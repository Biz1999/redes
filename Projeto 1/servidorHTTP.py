# HTTP/1.1 server template
import socket
import sys
from datetime import datetime
from page import sendPage


currentTime = datetime.now()
d = currentTime.ctime()
date_array = d.split()
data_formatada = f'Date: {date_array[0]}, {d[4:]} BRT\r\n'
nomes = []
# Porta
serverPort = 8081

# Criando socket
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind na porta
serverSocket.bind(('', serverPort))

# listening
serverSocket.listen(1)

print("Server HTTP/1.1 Initialized")
print(f'Listening to port {serverPort}')

# loop para receber as requisições

while True:
    connectionSocket, addr = serverSocket.accept()
    print("Client {} connected to server".format(addr))

    # Recebe a requisição
    request = connectionSocket.recv(1024).decode()

    # quebrando request
    request = request.split()

    if request:
        print(f'Requisição: {request}')

        if request[0] == "GET":
            params = request[1]

            if request[1] == '/' and len(request) > 4 or 'jpg' in request[1] and len(request) > 4:
                params = request[4]

            if params == f'localhost:{serverPort}':
                response = "\nHTTP/1.1 200 OK\r\n"
            else:
                response = "\nHTTP/1.1 404\r\n"
            response += data_formatada
            if request[1] == '/':
                response += "Content-Type:text/html; charset=UTF-8\r\n"
            else:
                response += "Content-Type:image/jpeg\r\n"
            response += "Connection: Keep-Alive\r\n\r\n"
            if params == f'localhost:{serverPort}' and request[1] == '/':
                response += sendPage('', 0)
            elif params != f'localhost:{serverPort}':
                response += sendPage('', 1)

            connectionSocket.send(response.encode())

            if 'jpg' in request[1]:
                image = request[1]
                image = image[image.find('/')+1:]
                image_to_read = open(image, 'rb')
                image_read = image_to_read.read()
                connectionSocket.send(image_read)

        if request[0] == "POST":
            params = request[1]
            if request[1] == '/' and len(request) > 4:
                params = request[4]

            params2 = request[-1]

            params_post = params2.split("&")
            params_fname = params_post[0][params2.find('=') + 1:]
            params_lname = params_post[1][params2.find('=') + 1:]

            nomes.append([params_fname, params_lname])

            print("Post type request, posting to {}".format(params))
            if params == f'localhost:{serverPort}':
                response = "\nHTTP/1.1 200 OK\r\n"
            else:
                response = "\nHTTP/1.1 404\r\n"
            response += data_formatada
            response += "Content-Type:text/html; charset=UTF-8\r\n"
            response += "Connection: Keep-Alive\r\n\r\n"
            if params == f'localhost:{serverPort}':
                response += sendPage(nomes, 0)
            else:
                response += sendPage('', 1)
            connectionSocket.send(response.encode())
