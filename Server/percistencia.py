from db import conexion

def persistencia(sql_query):
    cursor = conexion.cursor() #Insercion, eliminacion, actualizacion
    cursor.execute(sql_query)
    conexion.commit()
    cursor.close()
    return True

def persistencia_2(sql_query):
    cursor = conexion.cursor()
    cursor.execute(sql_query)
    resultado = cursor.fetchall() #Obtener todos los registros
    conexion.commit()
    cursor.close()
    return resultado