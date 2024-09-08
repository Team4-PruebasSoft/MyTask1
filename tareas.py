import pyodbc
from conexion import cursor

def MakeTareasBD():
    try:
        cursor.execute("SELECT name FROM master.dbo.sysdatabases")
        bases = cursor.fetchall()
        base_list = []
        for i in bases:
            base_list.append(i[0])
        if "Tareas" not in base_list:
            cursor.execute("CREATE DATABASE Tareas")
            cursor.execute("USE Tareas")
            cursor.execute("CREATE TABLE issues(id_tarea INT IDENTITY(1,1) PRIMARY KEY, titulo VARCHAR(255), descripcion VARCHAR(255), vencimiento DATE, etiqueta VARCHAR(255), estado VARCHAR(255))")
        cursor.execute("USE Tareas")
    except Exception as ex:
        print(ex)

def MakeIssue(titulo,desc,date,tag):
    fecha = date.strftime("%Y-%m-%d")
    issue_info = [titulo,desc,fecha,tag,"pendiente"]
    cursor.execute("INSERT INTO issues (titulo,descripcion,vencimiento,etiqueta,estado) VALUES (?,?,?,?,?)", issue_info)
    print("TAREA AGREGADA CORRECTAMENTE")