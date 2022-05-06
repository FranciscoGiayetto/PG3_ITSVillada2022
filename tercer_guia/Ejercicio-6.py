# mysql-connector-python (https://www.neoguias.com/como-conectarse-a-mysql-usando-python/)

import mysql.connector

miConexion = mysql.connector.connect(
    host="localhost", user="bdi", passwd="pepe1234", db="Biblioteca"
)
cur = miConexion.cursor()
try:
    cur.execute("SELECT * FROM Libro")
except mysql.connector.errors.ProgrammingError as e:
    print("Error")
    print(e)
    print(type(e))

miConexion.close()
