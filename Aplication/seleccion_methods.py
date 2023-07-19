import socket
import pickle

def crear_socket():
    mi_socket = socket.socket()
    mi_socket.connect(('localhost', 8000))
    return mi_socket
    
def generar_id_parametroEvaluacion():
    mi_socket = crear_socket()
    consultaParametros = "CONSULTAR_PARAMETROEVALUACION|PARAMETROEVALUACION|MAX(CODIGO_PEV)"
    mi_socket.send(consultaParametros.encode("utf-8"))
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

def generar_id_evaluacion():
    mi_socket = crear_socket()
    consultaParametros = "CONSULTAR_EVALUACION|EVALUACION|MAX(NUMERO_EVA)"
    mi_socket.send(consultaParametros.encode("utf-8"))
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

def consultar_candidatos():
    mi_socket = crear_socket()
    consultaCandidatos = "OBTENER_CANDIDATO|CANDIDATO|CEDULA_CAN,NOMBRE_CAN,APELLIDO_CAN,FECHANACIMIENTO_CAN"
    mi_socket.send(consultaCandidatos.encode("utf-8"))
    data = b''
    data += mi_socket.recv(1024)
    print(data)
    data_decoded = pickle.loads(data)
    print(data_decoded)
    return data_decoded

def consultar_parametrosevaluacion():
    mi_socket = crear_socket()
    consultaCandidatos = "OBTENER_PEV|PARAMETROEVALUACION|CEDULA_CAN,CODIGO_PEV,NOMBRE_PEV,PUNTAJEMAXIMO_PEV"
    mi_socket.send(consultaCandidatos.encode("utf-8"))
    data = b''
    data += mi_socket.recv(1024)
    print(data)
    data_decoded = pickle.loads(data)
    print(data_decoded)
    return data_decoded