import socket
from threading import Thread
from datetime import datetime

from Server import *
from responses.Get import GET
from responses.Post import POST
from responses.Put import PUT
from responses.Delete import DELETE


class ControlRequest(Thread):
    
    def __init__(self, server):
        Thread.__init__(self)
        self.server = server

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
                    GET.response(request, self.server, connectionSocket)

                elif request[0] == "POST":
                    POST.response(request, self.server, connectionSocket)

                elif request[0] == "PUT":
                    PUT.response(request, self.server, connectionSocket)

                elif request[0] == "DELETE":
                    DELETE.response(request, self.server, connectionSocket)

                connectionSocket.close()



