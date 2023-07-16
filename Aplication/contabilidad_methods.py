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
    print("-----Este es el resultado del tipo de cuenta")
    print(result)
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
    cursor = conexion.cursor()
    sql = "SELECT MAX(CODIGO_CUE) FROM cuenta"
    cursor.execute(sql)
    result = cursor.fetchone()

    if result[0] is None:
        id = "C01"  
    else:
        letras = ""
        numeros = ""
        for i in result[0]:
            if i.isalpha():
                letras += i
            else:
                numeros += i

        if numeros[0] == "0":
            cambio = int(numeros) + 1
            nuevo = str(cambio)
            nuevo = "0" + nuevo
            id = letras + nuevo
        else:
            cambio = int(numeros) + 1
            nuevo = str(cambio)
            id = letras + nuevo
    return id
