import socket
from modules.page import sendPage
from modules.filterDataToArray import filterDataToArray

class POST:
    @staticmethod
    def response(request, server, nomes, connection):
        params = request[1]
        if request[1] == '/' and len(request) > 4:
            params = request[4]

        params2 = request[-1]
        # print(params2)

        nomes = filterDataToArray(params2, nomes)

        print("Post type request, posting to {}".format(params))
        if params == f'localhost:{server.port}':
            response = "\nHTTP/1.1 200 OK\r\n"
        else:
            response = "\nHTTP/1.1 404\r\n"
        response += server.data
        response += "Content-Type:text/html; charset=UTF-8\r\n"
        response += "Connection: keep-alive\r\n\r\n"
        if params == f'localhost:{server.port}':
            response += sendPage(nomes, 0)
            # page = codecs.open("home.html", "r", "utf-8")
            # response+=page.read()
        else:
            response += sendPage(nomes, 1)
        connection.send(response.encode())
        