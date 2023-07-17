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
    if result  == "None":
        id = "1"  
    else:
        result = result[1:-1]
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
    result = result[3:-4]
    print(result)
    print(type(result))
    if result == "on":
        id = "1"  
    else:
        id = int(result)
        id += 1
        id = str(id)
    return id

def generar_id_asiento():
    mi_socket = crear_socket()
    consultaMotivos = "CONSULTAR|COMPROBANTE|MAX(CODIGO_COM)"
    mi_socket.send(consultaMotivos.encode("utf-8"))
    data = b''
    data += mi_socket.recv(1024)
    result = pickle.loads(data)
    result = str(result)
    result = result[3:-4]
    print(result)
    print(type(result))
    if result == "on":
        id = "1"  
    else:
        id = int(result)
        id += 1
        id = str(id)
    return id

def consultar_cuenta():
    mi_socket = crear_socket()
    consultaCuenta = "OBTENER_CUENTA|CUENTA"
    mi_socket.send(consultaCuenta.encode("utf-8"))
    data = b''
    data += mi_socket.recv(1024)
    print(data)
    result = pickle.loads(data)
    print(result)
    mi_socket.close()
    return result

