import socket
import pickle

def crear_socket():
    mi_socket = socket.socket()
    mi_socket.connect(('localhost', 8000))
    return mi_socket
    
def generar_id():
    mi_socket = crear_socket()
    consultaMotivos = "CONSULTAR_MOTIVO|MOTIVO|MAX(CAST(codigo_mot AS UNSIGNED))"
    mi_socket.send(consultaMotivos.encode("utf-8"))
    result = mi_socket.recv(1024).decode("utf-8")
    result = str(result)
    print(result)
    if result == "None":
        id = "1"  
    else:
        
        print(result)
        id = int(result)
        id += 1
        id = str(id)
    return id

def consultar_motivos():
    mi_socket = crear_socket()
    consultaMotivos = "OBTENER_MOTIVO|MOTIVO|CODIGO_MOT,NOMBRE_MOT"
    mi_socket.send(consultaMotivos.encode("utf-8"))
    data = b''
    data += mi_socket.recv(1024)
    print(data)
    data_decoded = pickle.loads(data)
    print(data_decoded)
    return data_decoded

def generar_id_detalle():
    mi_socket = crear_socket()
    consultaNomina = "CONSULTAR_NOMINA_DETALLE|NOMINA|MAX(CODIGO_NOM)"
    mi_socket.send(consultaNomina.encode("utf-8"))
    result = mi_socket.recv(1024).decode("utf-8")
    result = str(result)
    print(result)
    if result == "None":
        id = "1"  
    else:
        result = result[1:-1]
        id = int(result)
        id += 1
        id = str(id)
    return id

def consultar_empleados():
    mi_socket = crear_socket()
    consultaMotivos = "OBTENER_EMPLEADO|EMPLEADO|CEDULA_EMP,NOMBRE_EMP,APELLIDO_EMP"
    mi_socket.send(consultaMotivos.encode("utf-8"))
    data = b''
    data += mi_socket.recv(1024)
    print(data)
    data_decoded = pickle.loads(data)
    print(data_decoded)
    return data_decoded
