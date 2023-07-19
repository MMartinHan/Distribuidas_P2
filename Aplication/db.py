import mysql.connector

config = {
    'user': 'root',
    'password': 'root',
    'host': 'localhost',
    'database': 'proyectod',
}

# Establecer la conexión
conexion = mysql.connector.connect(**config)
