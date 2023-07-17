from db import conexion
import socket
import pickle

def crear_socket():
    mi_socket = socket.socket()
    mi_socket.connect(('localhost', 8000))
    return mi_socket

# Reglas del negocio para el módulo de SELECCIÓN

# Reglas del negocio para el módulo de NÓMINA

# Reglas del negocio para el módulo de CONTABILIDAD

def verificar_asiento(cantidad_debe, cantidad_haber):
    if cantidad_debe == cantidad_haber:
        return True
    else:
        return False
