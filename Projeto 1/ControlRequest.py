import socket
from threading import Thread
from datetime import datetime

from Server import *
from responses.Get import GET
from responses.Post import POST


class ControlRequest(Thread):
    
    def __init__(self, server):
        Thread.__init__(self)
        self.server = server
        self.nomes = []

    def run(self):

        while True:
            connectionSocket, addr = self.server.serverSocket.accept()
            print("Client {} connected to server".format(addr))
        
            # Recebe a requisição
            request = connectionSocket.recv(1024).decode()

            if not request:
                break
            else:
                # quebrando request
                request = request.split()

                
                print(f'Requisição: {request}')

                if request[0] == "GET":
                    GET.response(request, self.server, self.nomes, connectionSocket)

                if request[0] == "POST":
                    POST.response(request, self.server, self.nomes, connectionSocket)

                connectionSocket.close()



