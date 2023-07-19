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

def calcular13(sueldo):
    return sueldo / 12

def calcular14(sueldo):
    return 450 / 12

def calcularGastoFondoReserva(sueldo):
    return sueldo / 12

def calcularAportePatronal(sueldo):
    return sueldo * 0.1215

def aportePersonalPagar(sueldo):
    return sueldo * 0.0945

def aportePatronalPagar(sueldo):
    return sueldo * 0.1215

def nominaPagar(sueldo):
    return (sueldo+calcular13(sueldo)+calcular14(sueldo)+calcularGastoFondoReserva(sueldo)+calcularAportePatronal(sueldo))-(aportePersonalPagar(sueldo)+aportePatronalPagar(sueldo))

def calificacion_evaluacion(parametroA, parametroB, parametroC):
    calificacionA = parametroA * 0.3
    calificacionB = parametroB * 0.4
    calificacionC = parametroC * 0.3
    return calificacionA + calificacionB + calificacionC
