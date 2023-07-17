import socket
import pickle
import percistencia as per

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
        print(sql)
        if per.persistencia(sql) == True:
            conexion.send("Orden ejecutada con exito".encode("utf-8"))
        else:
            conexion.send("Error al ejecutar la orden".encode("utf-8"))


    #CANDIDATO
    elif sql_query[0]=="CONSULTAR_CAN":
        print("Consultar candidato")
        sql = "SELECT * fROM " + sql_query[1]
        print(sql)
        resultado = per.persistencia_2(sql)
        resultadoAux = pickle.dumps(resultado)
        print(resultadoAux)
        conexion.send(resultadoAux)
    elif sql_query[0]=="MODIFICAR_CAN":
        print("Modificar candidato")
        sql = "UPDATE " + sql_query[1] + " SET NOMBRE_CAN='" + sql_query[2] + "', APELLIDO_CAN='" + sql_query[3] + "', FECHANACIMIENTO_CAN='" + sql_query[4] + "' WHERE CEDULA_CAN=" + sql_query[5]
        print(sql)
        if per.persistencia(sql) == True:
            conexion.send("Orden ejecutada con exito".encode("utf-8"))
        else:
            conexion.send("Error al ejecutar la orden".encode("utf-8"))
    elif sql_query[0]=="ELIMINAR_CAN":
        print("Eliminar candidato")
        sql = "DELETE FROM " + sql_query[1] + " WHERE CEDULA_CAN=" + sql_query[2]
        if per.persistencia(sql) == True:
            conexion.send("Orden ejecutada con exito".encode("utf-8"))
        else:
            conexion.send("Error al ejecutar la orden".encode("utf-8"))
    #PARAMETROEVALUACION
    elif sql_query[0]=="OBTENER_CANDIDATO":
        print("Obtener candidato")
        sql = "SELECT CEDULA_CAN FROM " + sql_query[1]
        resultado = per.persistencia_2(sql)
        print(resultado)
        resultadoAux = pickle.dumps(resultado)
        print(resultadoAux)
        conexion.send(resultadoAux)
    elif sql_query[0]=="CONSULTAR_PARAMETRO":
        print("Consultar parametro de evaluación")
        sql = "SELECT * FROM " + sql_query[1]
        print(sql)
        resultado = per.persistencia_2(sql)
        resultadoAux = pickle.dumps(resultado)
        print(resultadoAux)
        conexion.send(resultadoAux)
    elif sql_query[0]=="CONSULTAR_PARAMETROEVALUACION":
        print("Consultar parametro de evaluación")
        sql = "SELECT " + sql_query[2] + " FROM " + sql_query[1] 
        resultado = per.persistencia_2(sql)
        print(resultado)
        resultado = str(resultado)
        resultado = resultado[2:-3]
        print(resultado)
        print(type(resultado))
        conexion.send(resultado.encode("utf-8"))
    elif sql_query[0]=="MODIFICAR_PARAMETRO":
        print("Modificar parametro de evaluación")
        sql = "UPDATE "+sql_query[1]+" SET CEDULA_CAN='"+sql_query[2]+"', NOMBRE_PEV='"+sql_query[3]+"', PUNTAJEMAXIMO_PEV='"+sql_query[4]+"' WHERE CODIGO_PEV="+sql_query[5]
        print(sql)
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
    
    elif sql_query[0] == "CONSULTAR_NOMINA_DETALLE":
        print("Consultar nomina detalle")
        sql = "SELECT "+sql_query[2]+" FROM " + sql_query[1]
        resultado = per.persistencia_2(sql)
        print(resultado)
        resultado = str(resultado)
        resultado = resultado[2:-3]
        print(resultado)
        print(type(resultado))
        conexion.send(resultado.encode("utf-8"))
    
    elif sql_query[0]=="OBTENER_EMPLEADO":
        print("Obtener motivo")
        sql = "SELECT "+sql_query[2]+" FROM " + sql_query[1]
        resultado = per.persistencia_2(sql)
        print(resultado)
        resultadoAux = pickle.dumps(resultado)
        print(resultadoAux)
        conexion.send(resultadoAux)
    
    elif sql_query[0]=="JOIN":
        print("Join")
        sql = "SELECT e.CODIGO_MOT, m.NOMBRE_MOT, e.CEDULA_EMP, e.NOMBRE_EMP, e.APELLIDO_EMP, e.FECHA_ING_EMP, e.SUELDO_EMP FROM EMPLEADO e JOIN MOTIVO m ON e.CODIGO_MOT = m.CODIGO_MOT"
        resultado = per.persistencia_2(sql)
        print(resultado)
        resultadoAux = pickle.dumps(resultado)
        print(resultadoAux)
        conexion.send(resultadoAux)
     
    elif sql_query[0]=="CONSULTA_REPORTE":
        sql = "SELECT * FROM " + sql_query[1]
        resultado = per.persistencia_2(sql)
        print(resultado)
        resultadoAux = pickle.dumps(resultado)
        print(resultadoAux)
        conexion.send(resultadoAux)
    
    elif sql_query[0]=="MODIFICAR_REPORTE":
        sql = "UPDATE "+sql_query[1]+" SET FECHA_NOM='"+sql_query[2]+"', DETALLE_NOM='"+sql_query[3]+"', SUELDO_EMP_NOM='"+sql_query[4]+"' WHERE CODIGO_NOM="+sql_query[5]
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
        
    conexion.close()