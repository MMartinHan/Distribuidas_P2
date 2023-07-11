import socket

mi_socket = socket.socket()
mi_socket.bind(('localhost', 8000))
mi_socket.listen(10)

while True:
    conexion, addr = mi_socket.accept()
    print("Nueva conexión establecida!")
    print(addr)
    
    conexion.send("Hola te saludo desde el servidor".encode("utf-8"))
    
    # Esperar la respuesta del cliente
    respuesta = conexion.recv(1024)
    print(respuesta)
    
    conexion.close()