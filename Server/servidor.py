import socket
import percistencia as per

mi_socket = socket.socket()
mi_socket.bind(('localhost', 8000))
mi_socket.listen(10)

while True:
    conexion, addr = mi_socket.accept()
    print("Nueva conexión establecida!")
    print(addr)
    
    conexion.send("Hola te saludo desde el servidor".encode("utf-8"))
    
    # Esperar la respuesta del cliente
    respuesta = conexion.recv(1024)
    respuesta = respuesta.decode("utf-8")
    sql_query = respuesta.split("|")
    values = sql_query[3].split(",")
    print(values)
    if sql_query[0]=="INGRESAR":
        print("Ingresar")
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
    
    conexion.close()