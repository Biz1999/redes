import socket
from modules.page import sendErrorPage

class GET:
    @staticmethod
    def response(request, server, connection):
        params = request[1]
        uri= {
            '/' : 'Content-Type:text/html; charset=utf-8',
            '/styles.css': 'Content-Type:text/css; charset=utf-8',
            '/styles_users.css': 'Content-Type:text/css; charset=utf-8',
            '/Server.json': 'Content-Type:application/json',
        }
        addr = ''
        uri_user = ''
        if params in uri.keys():
            addr = request[4]
        else:
            uri_user = params[params.find('/') + 1:]
            uri[params] = 'Content-Type:text/html; charset=utf-8'
            addr = request[4]

        if addr == f'localhost:{server.port}':
            response = "\nHTTP/1.1 200 OK\r\n"
        else:
            response = "\nHTTP/1.1 404\r\n"
        response += server.data
        response += "Connection: keep-alive\r\n"
        response += f'{uri.get(params)}\r\n\r\n'
        if addr == f'localhost:{server.port}' and params == '/':
            with open("pages/index.html", "r", encoding='utf-8') as f:
                text = f.read()
            response += text
            f.close()
        elif addr == f'localhost:{server.port}' and params == '/styles.css':
            css = open('styles/styles.css', 'r')
            response += css.read()
            css.close()
        elif addr == f'localhost:{server.port}' and params == '/styles_users.css':
            css = open('styles/styles_users.css', 'r')
            response += css.read()
            css.close()
        elif addr == f'localhost:{server.port}' and params == '/Server.json':
            json = open('db/Server.json', 'r')
            response += json.read()
            json.close()
        else:
            try:
                link = int(uri_user)
                if addr == f'localhost:{server.port}' and link:
                    with open(f"pages/users/{uri_user}.html", "r", encoding='utf-8') as f:
                        text = f.read()
                response += text
                f.close()
            except:
                response += sendErrorPage()
        
        connection.send(response.encode())

