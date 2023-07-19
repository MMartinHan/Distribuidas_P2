import mysql.connector

config = {
    'user': 'root',
<<<<<<< HEAD
    'password': 'root',
=======
    'password': '12345',
>>>>>>> 03c32abaffeae74e5feae4f14c94674fed347d6f
    'host': 'localhost',
    'database': 'proyectod',
}

# Establecer la conexión
conexion = mysql.connector.connect(**config)