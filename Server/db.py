import mysql.connector

config = {
    'user': 'root',
    'password': '12345',
    'host': 'localhost',
    'database': 'proyectod',
}

# Establecer la conexión
conexion = mysql.connector.connect(**config)