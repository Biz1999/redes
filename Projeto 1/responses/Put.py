import socket
from modules.page import sendPage
from modules.updateJson import update_json
import json


class PUT:

    @staticmethod
    def response(request, server, connection):
        params = request[1]
        if request[1] == '/' and len(request) > 4:
            params = request[4]

        params2 = request[-1]
        params2 = json.loads(params2)
        update_json(params2)

        if params == f'localhost:{server.port}':
            response = "\nHTTP/1.1 200 OK\r\n"
        else:
            response = "\nHTTP/1.1 404\r\n"
        response += server.data
        response += "Connection: keep-alive\r\n\r\n"
        if params != f'localhost:{server.port}':
            response += sendPage(1)

        connection.send(response.encode())
