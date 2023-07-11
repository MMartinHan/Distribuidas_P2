from db import conexion

def insertar_motivo():
    cursor = conexion.cursor()
    sql = "INSERT INTO motivo (CODIGO_MOT,NOMBRE_MOT) VALUES (%s,%s)"
    datos = ("M02","motivo")
    cursor.execute(sql, datos)
    conexion.commit()
    print("Datos guardados")
    conexion.close()