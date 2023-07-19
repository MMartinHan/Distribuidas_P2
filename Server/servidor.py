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
    # Esperar la respuesta del cliente
    respuesta = conexion.recv(1024)
    respuesta = respuesta.decode("utf-8")
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

    elif sql_query[0]=="COMPROBAR_USUARIO":
        print("Comprobar usuario")
        sql = "SELECT * FROM " + sql_query[1] + " WHERE NOMBRE_USU='" + sql_query[2] + "' AND CLAVE_USU='" + sql_query[3] + "'"
        print(sql)
        resultado = per.persistencia_2(sql)
        resultadoAux = pickle.dumps(resultado)
        print(resultadoAux)
        conexion.send(resultadoAux)
    
    elif sql_query[0]=="OBTENER_USUARIOS":
        print("Obtener usuarios")
        sql = "SELECT NOMBRE_USU FROM " + sql_query[1] + " WHERE NOMBRE_USU='" + sql_query[2] + "'"
        print(sql)
        resultado = per.persistencia_2(sql)
        resultadoAux = pickle.dumps(resultado)
        print(resultadoAux)
        conexion.send(resultadoAux)
        
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
    elif sql_query[0]=="OBTENER_PEV":
        print("Obtener candidato")
        sql = "SELECT CEDULA_CAN, CODIGO_PEV FROM " + sql_query[1]
        resultado = per.persistencia_2(sql)
        print(resultado)
        resultadoAux = pickle.dumps(resultado)
        print("datos cb")
        print(resultadoAux)
        conexion.send(resultadoAux)
    elif sql_query[0]=="MODIFICAR_PARAMETRO":
        print("Modificar parametro de evaluación")
        sql = "UPDATE "+sql_query[1]+" SET CEDULA_CAN='"+sql_query[2]+"', NOMBRE_PEV='"+sql_query[3]+"', PUNTAJEMAXIMO_PEV='"+sql_query[4]+"' WHERE CODIGO_PEV="+sql_query[5]
        print(sql)
        if per.persistencia(sql) == True:
            conexion.send("Orden ejecutada con exito".encode("utf-8"))
        else:
            conexion.send("Error al ejecutar la orden".encode("utf-8"))
    #EVALUACION
    elif sql_query[0]=="OBTENER_PARAMETROEVALUACION":
        print("Obtener parametro de evaluacion")
        sql = "SELECT CEDULA_CAN, CODIGO_PEV FROM " + sql_query[1] 
        resultado = per.persistencia_2(sql)
        print(resultado)
        resultadoAux = pickle.dumps(resultado)
        print(resultadoAux)
        conexion.send(resultadoAux)
    elif sql_query[0]=="CONSULTAR_EVA":
        sql = "SELECT " + sql_query[2] + " FROM " + sql_query[1]
        resultado = per.persistencia_2(sql)
        resultadoAux = pickle.dumps(resultado)
        print(resultadoAux)
        conexion.send(resultadoAux)
    elif sql_query[0]=="CONSULTAR_EVALUACION":
        print("Consultar evaluación")
        sql = "SELECT " + sql_query[2] + " FROM " + sql_query[1] 
        resultado = per.persistencia_2(sql)
        print(resultado)
        resultado = str(resultado)
        resultado = resultado[2:-3]
        print(resultado)
        print(type(resultado))
        conexion.send(resultado.encode("utf-8"))
    

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
    
    elif sql_query[0]=="CONSULTAR_ESPECIFICO":
        sql = "SELECT * FROM " + sql_query[1] + " WHERE " + sql_query[2] + " = '" + sql_query[3]+"'"
        print(sql)
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
    
    elif sql_query[0]=="CONSULTAR_EMPLEADO_CED":
        print("Consultar empleado")
        sql="SELECT * FROM "+sql_query[1]+" WHERE CEDULA_EMP='"+sql_query[3]+"'"
        print(sql)
        resultado = per.persistencia_2(sql)
        resultadoAux = pickle.dumps(resultado)
        print(resultadoAux)
        conexion.send(resultadoAux) 
            
    elif sql_query[0]=="CONSULTAR_REPORTE_COD":
        print("Consultar reporte")
        sql="SELECT * FROM "+sql_query[1]+" WHERE CODIGO_NOM='"+sql_query[3]+"'"
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
    
    elif sql_query[0] == "CONSULTA_SALARIOS":
        print("Consultar sueldo")
        sql = "SELECT CEDULA_EMP, NOMBRE_EMP, APELLIDO_EMP, SUELDO_EMP FROM " + sql_query[1]
        resultado = per.persistencia_2(sql)
        print(resultado)
        resultadoAux = pickle.dumps(resultado)
        print(resultado)
        print(type(resultado))
        conexion.send(resultadoAux)
    
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
        sql = "SELECT * FROM " + sql_query[1] + " ORDER BY (CODIGO_NOM)"
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
    elif sql_query[0]=="CONSULTAR_TC_NOMBRE":
        sql = "SELECT * FROM " + sql_query[1] + " WHERE NOMBRE_TC='" + sql_query[3] + "'"
        print(sql)
        resultado = per.persistencia_2(sql)
        print(resultado)
        resultadoAux = pickle.dumps(resultado)
        print(resultadoAux)
        conexion.send(resultadoAux)
    elif sql_query[0]=="CONSULTAR_CUENTA_NOMBRE":
        sql = "SELECT * FROM " + sql_query[1] + " WHERE NOMBRE_CUE='" + sql_query[3] + "'"
        print(sql)
        resultado = per.persistencia_2(sql)
        print(resultado)
        resultadoAux = pickle.dumps(resultado)
        print(resultadoAux)
        conexion.send(resultadoAux)
    elif sql_query[0]=="CONSULTAR_COMPROBANTE_OBSERVACION":
        sql = "SELECT CODIGO_COM, FECHA_COM, OBSERVACIONES_COM FROM " + sql_query[1] + " WHERE OBSERVACIONES_COM='" + sql_query[3] + "'"
        print(sql)
        resultado = per.persistencia_2(sql)
        print(resultado)
        resultadoAux = pickle.dumps(resultado)
        print(resultadoAux)
        conexion.send(resultadoAux)
    elif sql_query[0]=="OBTENER_NOMBRE_CUE":
        print("Obtener nombre tipo cuenta")
        sql = "SELECT "+sql_query[2]+" FROM " + sql_query[1] + " WHERE CODIGO_CUE=" + sql_query[3]
        resultado = per.persistencia_2(sql)
        print(resultado)
        resultadoAux = pickle.dumps(resultado)
        print(resultadoAux)
        conexion.send(resultadoAux)
    elif sql_query[0]=="OBTENER_CODIGO_TC":
        print("Obtener codigo tipo cuenta")
        sql = "SELECT "+sql_query[2]+" FROM " + sql_query[1] + " WHERE NOMBRE_TC='" + sql_query[3] + "'"
        print(sql)
        resultado = per.persistencia_2(sql)
        print(resultado)
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
    elif sql_query[0]=="CONSULTAR_COMPROBANTE":
        sql = "SELECT "+sql_query[2]+" FROM "+sql_query[1]+" WHERE CODIGO_COM = "+sql_query[3]
        print(sql)
        resultado = per.persistencia_2(sql)
        resultadoAux = pickle.dumps(resultado)
        print(resultadoAux)
        conexion.send(resultadoAux)
    elif sql_query[0]=="CONSULTAR_INGRESOS":
        sql = "SELECT CODIGO_CUE, CANTIDAD_DEBE_COM, CANTIDAD_HABER_COM FROM "+sql_query[1]+" WHERE CODIGO_TC = '3' AND FECHA_COM > '"+sql_query[2] + "' AND FECHA_COM < '"+sql_query[3] + "'"
        print(sql)
        resultado = per.persistencia_2(sql)
        resultadoAux = pickle.dumps(resultado)
        print(resultadoAux)
        conexion.send(resultadoAux)
    elif sql_query[0]=="CONSULTAR_GASTOS":
        sql = "SELECT CODIGO_CUE, CANTIDAD_DEBE_COM, CANTIDAD_HABER_COM FROM "+sql_query[1]+" WHERE CODIGO_TC = '1' AND FECHA_COM > '"+sql_query[2] + "' AND FECHA_COM < '"+sql_query[3] + "'"
        print(sql)
        resultado = per.persistencia_2(sql)
        resultadoAux = pickle.dumps(resultado)
        print(resultadoAux)
        conexion.send(resultadoAux)
    elif sql_query[0]=="MODIFICAR_COMPROBANTE":
        sql = "UPDATE "+sql_query[1]+" SET FECHA_COM='"+sql_query[4]+"', OBSERVACIONES_COM='"+sql_query[5]+"', CANTIDAD_DEBE_COM="+sql_query[6]+", CANTIDAD_HABER_COM="+sql_query[7]+" WHERE CODIGO_COM="+sql_query[8] + " AND CODIGO_TC="+sql_query[2] + " AND CODIGO_CUE="+sql_query[3]
        print(sql)
        if per.persistencia(sql) == True:
            conexion.send("Orden ejecutada con exito".encode("utf-8"))
        else:
            conexion.send("Error al ejecutar la orden".encode("utf-8"))
    elif sql_query[0]=="VERIFICAR_ASIENTO":
        bandera = rn.verificar_asiento(sql_query[1], sql_query[2])
        bandera = int(bandera)
        conexion.send(bandera.to_bytes(1,'big'))
    elif sql_query[0]=="ELIMINAR_COMPROBANTE":
        sql = "DELETE FROM "+sql_query[1]+" WHERE CODIGO_COM="+sql_query[2]
        resultado = per.persistencia(sql)
        resultadoAux = pickle.dumps(resultado)
        print(resultadoAux)
        conexion.send(resultadoAux)
    elif sql_query[0]=="OBTENER_ASIENTO_AUTOMATICO":
        print("Obtener asiento automatico")
        listaAsiento = []
        sueldo13 = rn.calcular13(float(sql_query[1]))
        sueldo14 = rn.calcular14(float(sql_query[1]))
        gastoFondoReserva = rn.calcularGastoFondoReserva(float(sql_query[1]))
        gastoAportePatronal = rn.calcularAportePatronal(float(sql_query[1]))
        aportePersonalPagar = rn.aportePersonalPagar(float(sql_query[1]))
        aportePatronalPagar = rn.aportePatronalPagar(float(sql_query[1]))
        nominaPagar = rn.nominaPagar(float(sql_query[1]))
        listaAsiento.append(sueldo13)
        listaAsiento.append(sueldo14)
        listaAsiento.append(gastoFondoReserva)
        listaAsiento.append(gastoAportePatronal)
        listaAsiento.append(aportePersonalPagar)
        listaAsiento.append(aportePatronalPagar)
        listaAsiento.append(nominaPagar)
        resultadoAux = pickle.dumps(listaAsiento)
        conexion.send(resultadoAux)
        
    conexion.close()