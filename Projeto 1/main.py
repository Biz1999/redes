from Server import Server


def main():
    server = Server('localhost', 8081)
    print("Server HTTP/1.1 Initialized")
    print(f'Listening to port {server.port}')

if __name__ == "__main__":
    main()