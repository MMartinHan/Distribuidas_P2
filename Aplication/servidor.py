import socket

class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def start(self):
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(10)
        print("Servidor escuchando en {}:{}".format(self.host, self.port))

        while True:
            client_socket, client_address = self.server_socket.accept()
            print("Cliente conectado:", client_address)

            # Procesar la conexión entrante en un hilo o realizar alguna tarea
            # Aquí puedes manejar la conexión como desees, por ejemplo, iniciar un nuevo hilo para manejarla

            # Ejemplo: Enviar un mensaje de bienvenida al cliente
            welcome_message = "¡Bienvenido al servidor!"
            client_socket.sendall(welcome_message.encode())

            # Cerrar la conexión con el cliente
            client_socket.close()

    def stop(self):
        self.server_socket.close()

server = Server('localhost', 8000)
server.start()