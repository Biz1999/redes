import socket
from threading import Thread
from datetime import datetime

from Server import *
from responses.Get import GET
from responses.Post import POST
from responses.Put import PUT


class ControlRequest(Thread):
    
    def __init__(self, server):
        Thread.__init__(self)
        self.server = server
        self.nomes = []

    def run(self):

        while True:
            connectionSocket, addr = self.server.serverSocket.accept()
        
            # Recebe a requisição
            request = connectionSocket.recv(1024).decode()

            if request:
                # quebrando request

                request = request.split()
                print(f'Requisição: {request}')

                if request[0] == "GET":
                    GET.response(request, self.server, self.nomes, connectionSocket)

                elif request[0] == "POST":
                    POST.response(request, self.server, self.nomes, connectionSocket)

                elif request[0] == "PUT":
                    PUT.response(request, self.server, self.nomes, connectionSocket)

                connectionSocket.close()



