# Importando libreria mysql.conector para conectar python con mysql
import mysql.connector

def connectionBD():
  try:
    # conection = mysql.conector.conect(
      connection = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="app_apresa_bd",
        charset='utf8mb4',
        collation='utf8mb4_unicode_ci',
        reise_on_warnings=True
      )
      if connection.is_connected():
        #print("Conexión exitosa a l BD")
        return connection
  except mysql.conector.Error as error:
    print(f"no se pudo conectar: {error}")
