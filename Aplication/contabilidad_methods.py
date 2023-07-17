from db import conexion
import socket
import pickle

def crear_socket():
    mi_socket = socket.socket()
    mi_socket.connect(('localhost', 8000))
    return mi_socket

def consultar_tipo_cuenta():
    mi_socket = crear_socket()
    consultaTipoCuenta = "CONSULTAR_TIPO_CUENTA|TIPO_CUENTA|*"
    mi_socket.send(consultaTipoCuenta.encode("utf-8"))
    data = b''
    data += mi_socket.recv(1024)
    result = pickle.loads(data)
    mi_socket.close()
    return result
    
def generar_id_tipo_cuenta():
    mi_socket = crear_socket()
    consultaTipoCuenta = "CONSULTAR_TIPO_CUENTA_ID|TIPO_CUENTA|MAX(CODIGO_TC)"
    mi_socket.send(consultaTipoCuenta.encode("utf-8"))
    data = b''
    data += mi_socket.recv(1024)
    result = pickle.loads(data)
    result = str(result)
    print(result)
    if result  == "None":
        id = "1"  
    else:
        result = result[1:-1]
        print(result)
        id = int(result)
        id += 1
        id = str(id)
    return id

def generar_id_cuenta():
    mi_socket = crear_socket()
    consultaMotivos = "CONSULTAR|CUENTA|MAX(CODIGO_CUE)"
    mi_socket.send(consultaMotivos.encode("utf-8"))
    data = b''
    data += mi_socket.recv(1024)
    result = pickle.loads(data)
    result = str(result)
    print(result)
    if result == "None":
        id = "1"  
    else:
        result = result[3:-4]
        print(result)
        id = int(result)
        id += 1
        id = str(id)
    return id
