import socket
import pickle
import percistencia as per
import reglas_negocio as rn

mi_socket = socket.socket()
mi_socket.bind(('localhost', 8000))
mi_socket.listen(10)

while True:
    conexion, addr = mi_socket.accept()
    print("Nueva conexión establecida!")
    print(addr)
    # Esperar la respuesta del cliente
    respuesta = conexion.recv(1024)
    respuesta = respuesta.decode("utf-8")
    print(respuesta)
    print(respuesta)
    sql_query = respuesta.split("|")
    if sql_query[0]=="INGRESAR":
        print("Ingresar")
        values = sql_query[3].split(",")
        print(values)
        sql = "INSERT INTO "+sql_query[1]+" "+sql_query[2]+" "+"VALUES"+" ("
        for i in range(len(values)):
            sql = sql + "'"+values[i]+"',"
        sql = sql[:-1]
        sql = sql + ")"
        if per.persistencia(sql) == True:
            conexion.send("Orden ejecutada con exito".encode("utf-8"))
        else:
            conexion.send("Error al ejecutar la orden".encode("utf-8"))
    elif sql_query[0]=="CONSULTAR":
        sql = "SELECT " + sql_query[2] + " FROM " + sql_query[1]
        resultado = per.persistencia_2(sql)
        resultadoAux = pickle.dumps(resultado)
        print(resultadoAux)
        conexion.send(resultadoAux)
    elif sql_query[0]=="CONSULTAR_MOTIVO":
        print("Consultar motivo")
        sql = "SELECT " + sql_query[2] + " FROM " + sql_query[1] 
        resultado = per.persistencia_2(sql)
        print(resultado)
        resultado = str(resultado)
        resultado = resultado[2:-3]
        print(resultado)
        print(type(resultado))
        conexion.send(resultado.encode("utf-8"))
    elif sql_query[0]=="MODIFICAR":
        print("Modificar")
        sql = "UPDATE " + sql_query[1] + " SET NOMBRE_MOT='" + sql_query[2] + "' WHERE CODIGO_MOT=" + sql_query[3]
        if per.persistencia(sql) == True:
            conexion.send("Orden ejecutada con exito".encode("utf-8"))
        else:
            conexion.send("Error al ejecutar la orden".encode("utf-8"))
    elif sql_query[0]=="ELIMINAR":
        print("Eliminar")
        sql = "DELETE FROM " + sql_query[1] + " WHERE "+sql_query[2]+" =" + sql_query[3]
        if per.persistencia(sql) == True:
            conexion.send("Orden ejecutada con exito".encode("utf-8"))
        else:
            conexion.send("Error al ejecutar la orden".encode("utf-8"))
    elif sql_query[0]=="OBTENER_MOTIVO":
        print("Obtener motivo")
        sql = "SELECT * FROM " + sql_query[1]
        resultado = per.persistencia_2(sql)
        print(resultado)
        resultadoAux = pickle.dumps(resultado)
        print(resultadoAux)
        conexion.send(resultadoAux)
    elif sql_query[0]=="CONSULTAR_EMPLEADO":
        print("Consultar empleado")
        sql = "SELECT * FROM " + sql_query[1]
        print(sql)
        resultado = per.persistencia_2(sql)
        resultadoAux = pickle.dumps(resultado)
        print(resultadoAux)
        conexion.send(resultadoAux)
    elif sql_query[0]=="MODIFICAR_EMPLEADO":
        print("Modificar empleado")
        sql = "UPDATE "+sql_query[1]+" SET CODIGO_MOT='"+sql_query[2]+"', NOMBRE_EMP='"+sql_query[3]+"', APELLIDO_EMP='"+sql_query[4]+"', FECHA_ING_EMP='"+sql_query[5]+"', SUELDO_EMP='"+sql_query[6]+"' WHERE CEDULA_EMP="+sql_query[7]
        print(sql)
        if per.persistencia(sql) == True:
            conexion.send("Orden ejecutada con exito".encode("utf-8"))
        else:
            conexion.send("Error al ejecutar la orden".encode("utf-8"))
    elif sql_query[0]=="CONSULTAR_TIPO_CUENTA":
        print("Consultar tipo cuenta")
        sql = "SELECT " + sql_query[2] + " FROM " + sql_query[1] 
        resultado = per.persistencia_2(sql)
        resultadoAux = pickle.dumps(resultado)
        print(resultado)
        print(type(resultado))
        conexion.send(resultadoAux)
    elif sql_query[0]=="CONSULTAR_TIPO_CUENTA_ID":
        print("Consultar tipo cuenta")
        sql = "SELECT " + sql_query[2] + " FROM " + sql_query[1] 
        resultado = per.persistencia_2(sql)
        resultado = str(resultado)
        resultado = resultado[2:-3]
        resultadoAux = pickle.dumps(resultado)
        print(resultado)
        print(type(resultado))
        conexion.send(resultadoAux)
    elif sql_query[0]=="ELIMINAR_TC":
        print("Eliminar")
        sql = "DELETE FROM " + sql_query[1] + " WHERE CODIGO_TC=" + sql_query[2]
        if per.persistencia(sql) == True:
            conexion.send("Orden ejecutada con exito".encode("utf-8"))
        else:
            conexion.send("Error al ejecutar la orden".encode("utf-8"))
    elif sql_query[0]=="MODIFICAR_TC":
        print("Modificar")
        sql = "UPDATE " + sql_query[1] + " SET NOMBRE_TC='" + sql_query[2] + "' WHERE CODIGO_TC=" + sql_query[3]
        print(sql)
        if per.persistencia(sql) == True:
            conexion.send("Orden ejecutada con exito".encode("utf-8"))
        else:
            conexion.send("Error al ejecutar la orden".encode("utf-8"))
    elif sql_query[0]=="MODIFICAR_CUENTA":
        sql = "UPDATE "+sql_query[1]+" SET CODIGO_TC='"+sql_query[2]+"', NOMBRE_CUE='"+sql_query[4]+"' WHERE CODIGO_CUE="+sql_query[3]
        if per.persistencia(sql) == True:
            conexion.send("Orden ejecutada con exito".encode("utf-8"))
        else:
            conexion.send("Error al ejecutar la orden".encode("utf-8"))
    elif sql_query[0]=="OBTENER_CUENTA":
        print("Obtener cuenta")
        sql = "SELECT * FROM " + sql_query[1]
        resultado = per.persistencia_2(sql)
        print(resultado)
        resultadoAux = pickle.dumps(resultado)
        print(resultadoAux)
        conexion.send(resultadoAux)
    elif sql_query[0]=="OBTENER_NOMBRE_TC":
        print("Obtener nombre tipo cuenta")
        sql = "SELECT "+sql_query[2]+" FROM " + sql_query[1] + " WHERE CODIGO_TC=" + sql_query[3]
        resultado = per.persistencia_2(sql)
        print(resultado)
        resultadoAux = pickle.dumps(resultado)
        print(resultadoAux)
        conexion.send(resultadoAux)
    elif sql_query[0]=="OBTENER_CODIGO_TC":
        print("Obtener codigo tipo cuenta")
        sql = "SELECT "+sql_query[2]+" FROM " + sql_query[1] + " WHERE NOMBRE_TC='" + sql_query[3] + "'"
        resultado = per.persistencia_2(sql)
        resultadoAux = pickle.dumps(resultado)
        print(resultadoAux)
        conexion.send(resultadoAux)
    elif sql_query[0]=="OBTENER_CODIGO_CUENTA":
        print("Obtener codigo tipo cuenta")
        sql = "SELECT "+sql_query[2]+" FROM " + sql_query[1] + " WHERE NOMBRE_CUE='" + sql_query[3] + "'"
        resultado = per.persistencia_2(sql)
        resultadoAux = pickle.dumps(resultado)
        print(resultadoAux)
        conexion.send(resultadoAux)
    elif sql_query[0]=="OBTENER_ASIENTOS":
        print("Obtener asientos")
        sql = "SELECT "+sql_query[2]+", "+sql_query[3]+", "+sql_query[4]+" FROM " + sql_query[1]
        resultado = per.persistencia_2(sql)
        resultadoAux = pickle.dumps(resultado)
        print(resultadoAux)
        conexion.send(resultadoAux)
    elif sql_query[0]=="VERIFICAR_ASIENTO":
        bandera = rn.verificar_asiento(sql_query[1], sql_query[2])
        bandera = int(bandera)
        conexion.send(bandera.to_bytes(1,'big'))
    conexion.close()