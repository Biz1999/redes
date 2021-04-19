#HTTP/1.1 server template
import socket
import sys
import codecs
from datetime import datetime

def sendPage( nome, error ):

    # data e horário
    date = (f'{datetime.now():%m-%Y %H:%M}')

    #código da página
    page = f'''<!DOCTYPE HTML>\n<html> 
        <body>
            <h1>This is THE WEB PAGE</h1> 
            <br>
            Hello World!
            <form method='POST'>
                <label style='background-color:red'>Primeiro nome:</label><br>
                <input type="text" name="fname"><br>
                <label>Sobrenome:</label><br>
                <input type="text" name="lname"><br><br>
                <input type="submit" value="Submit">
            </form> 
            <br>{date}<br>
            {nome}
        </body>
        </html>\r\n\r\n'''
    page404 = '''<!DOCTYPE HTML>\n<html>
        <body>
            <h1>
            ERRO 404<br>Pagina nao encontrada
            </h1>
        </body>
        </html>\r\n\r\n'''
    return (page if error==0 else page404)





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

        if params == f'localhost:{serverPort}':
            response = "\nHTTP/1.1 200 OK\r\n"
        else:
            response = "\nHTTP/1.1 404\r\n"
        response += data_formatada 
        response += "Connection: Keep-Alive\r\n"
        response += "Content-Type:text/html; charset=UTF-8\r\n\r\n"
        if params == f'localhost:{serverPort}':
            response += sendPage('', 0)
        else:
            response += sendPage('', 1)
        connectionSocket.send(response.encode())

    if request[0] == "POST":

        params = request[1]
        if request[1] == '/' and len(request) > 4:
            params = request[4]
            
        print(request)
        params2 = request[-1]

        params_post = params2.split("&")
        params_fname = params_post[0][params2.find('=') + 1:]
        params_lname = params_post[1][params2.find('=') + 1:]

        nome = f'{params_fname} {params_lname}'

        print("Post type request, posting to {}".format(params))
        if params == f'localhost:{serverPort}':
            response = "\nHTTP/1.1 200 OK\r\n"
        else:
            response = "\nHTTP/1.1 404\r\n"
        response += data_formatada 
        response += "Connection: Keep-Alive\r\n"
        response += "Content-Type:text/html; charset=UTF-8\r\n\r\n"
        if params == f'localhost:{serverPort}':
            response += sendPage(nome, 0)
        else:
            response += sendPage('', 1)
        connectionSocket.send(response.encode())

