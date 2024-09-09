import pyodbc
from conexion import cursor
import logging
import logger_config

def MakeUsersBD():
    try:
        cursor.execute("SELECT name FROM master.dbo.sysdatabases")
        bases = cursor.fetchall()
        base_list = []
        for i in bases:
            base_list.append(i[0])
        if "Users" not in base_list:
            cursor.execute("CREATE DATABASE Users")
            cursor.execute("USE Users")
            cursor.execute("CREATE TABLE usuarios(user_id INT IDENTITY(1,1) PRIMARY KEY, username VARCHAR(255) COLLATE SQL_Latin1_General_CP1_CS_AS NOT NULL, password VARCHAR(255) COLLATE SQL_Latin1_General_CP1_CS_AS NOT NULL)")
        cursor.execute("USE Users")
    except Exception as ex: 
        logging.error(f"Error al buscar y/o crear la base de datos 'Users'.: {ex}")

def Register(user, password): 
    try:
        userinfo = [user,password]
        cursor.execute("SELECT * FROM usuarios WHERE username=? AND password =?", userinfo)
        res = cursor.fetchone()
        if res is None:
            cursor.execute("INSERT INTO usuarios (username,password) VALUES (?,?)", userinfo)
            print("REGISTRO EXITOSO")
        else:
            print("USUARIO YA REGISTRADO")
    except Exception as ex:
        logging.error(f"Error al registrar el usuario: {ex}")
        print("ERROR AL REGISTRAR EL USUARIO")

def Login (user, password):
    try:
        userinfo = [user,password]
        cursor.execute("SELECT * FROM usuarios WHERE username=? AND password =?", userinfo)
        res = cursor.fetchone()
        if res is not None:
            return True
    except Exception as ex:
        logging.error(f"Error al iniciar sesión: {ex}")
        return False