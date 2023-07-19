import mysql.connector

config = {
    'user': 'root',
<<<<<<< HEAD
    'password': 'aagonzalez8',
=======
    'password': '12345',
>>>>>>> b1d94f8d4c02d93564d58c36f306f0116171f8ef
    'host': 'localhost',
    'database': 'proyectod',
}

# Establecer la conexión
conexion = mysql.connector.connect(**config)