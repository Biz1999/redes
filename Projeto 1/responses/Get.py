import socket
from modules.page import sendPage

class GET:
    @staticmethod
    def response(request, server, nomes, connection):
        params = request[1]

        if request[1] == '/' and len(request) > 4 or 'jpg' in request[1] and len(request) > 4:
            params = request[4]

        """ if "If-Modified-Since:" in request:
            response = "\nHTTP/1.1 304 Not Modified\r\n"
            connection.send(response.encode())
        else: """
        if params == f'localhost:{server.port}':
            response = "\nHTTP/1.1 200 OK\r\n"
        else:
            response = "\nHTTP/1.1 404\r\n"
        response += server.data
        response += "Connection: keep-alive\r\n"
        if request[1] == '/':
            response += "Content-Type:text/html; charset=UTF-8\r\n\r\n"
        elif 'jpg' in request[1]:
            response += "Content-Type:image/jpeg\r\n\r\n"
        # response += f"Last-Modified: {server.data}\r\n\r\n"

        if params == f'localhost:{server.port}' and request[1] == '/':
            response += sendPage(nomes, 0)
        elif params != f'localhost:{server.port}':
            response += sendPage(nomes, 1)
        
        connection.send(response.encode())

        if 'jpg' in request[1]:
            image = request[1]
            image = image[image.find('/')+1:]
            image_to_read = open(image, 'rb')
            image_read = image_to_read.read()
            connection.send(image_read)
    
        