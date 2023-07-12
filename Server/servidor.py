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
    elif sql_query[0]=="CONSULTAR":
        print("Consultar")
        sql = "SELECT " + sql_query[2] + " FROM " + sql_query[1]
        print(sql)
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
    conexion.close()