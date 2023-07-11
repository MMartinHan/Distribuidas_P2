from db import conexion
    
def generar_id():
    cursor = conexion.cursor()
    sql = "SELECT MAX(CODIGO_MOT) FROM motivo"
    cursor.execute(sql)
    result = cursor.fetchone()

    if result[0] is None:
        id = "M01"  
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