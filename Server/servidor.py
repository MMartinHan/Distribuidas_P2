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
    print(type(respuesta))
    print(type(sql_query))
    print(sql_query)
    print(type(sql_query[3]))
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
        per.persistencia(sql)
    
    conexion.close()