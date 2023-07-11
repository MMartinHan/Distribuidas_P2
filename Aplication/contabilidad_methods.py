from db import conexion

def insertar_cuenta():
    cursor = conexion.cursor()
    sql = "INSERT INTO motivo (CODIGO_MOT,NOMBRE_MOT) VALUES (%s,%s)"
    datos = ("M02","motivo")
    cursor.execute(sql, datos)
    conexion.commit()
    print("Datos guardados")
    conexion.close()
    
def generar_id_tipo_cuenta():
    cursor = conexion.cursor()
    sql = "SELECT MAX(CODIGO_TC) FROM tipo_cuenta"
    cursor.execute(sql)
    result = cursor.fetchone()

    if result[0] is None:
        id = "TC01"  
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
