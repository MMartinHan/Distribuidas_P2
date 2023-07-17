import mysql.connector

config = {
    'user': 'root',
    'password': 'aagonzalez8',
    'host': 'localhost',
    'database': 'proyectod',
}

# Establecer la conexión
conexion = mysql.connector.connect(**config)