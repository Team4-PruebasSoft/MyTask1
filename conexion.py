import pyodbc
import logging 
import logger_config 


try: 
    logging.info("Conectando a la base de datos.")
    connection = pyodbc.connect("DRIVER={SQL SERVER}; SERVER=KuVe-PC\SQLEXPRESS;Trusted_Connection=yes", autocommit=True)
    cursor = connection.cursor()
    logging.info("Conexión exitosa.")
except Exception as ex:
    logging.error(f"Error al conectar a la base de datos: {ex}")
    exit()
