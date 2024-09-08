import pyodbc

try:
    connection = pyodbc.connect("DRIVER={SQL SERVER}; SERVER=KuVe-PC\SQLEXPRESS;Trusted_Connection=yes", autocommit = True)
    cursor = connection.cursor()
    cursor.execute("SELECT name FROM master.dbo.sysdatabases")
    bases = cursor.fetchall()
    base_list = []
    for i in bases:
        base_list.append(i[0])
    if "Tareas" not in base_list:
        cursor.execute("CREATE DATABASE Tareas")
        cursor.execute("USE Tareas")
        cursor.execute("CREATE TABLE issues(id_tarea INT IDENTITY(1,1) PRIMARY KEY, titulo VARCHAR(255), descripcion VARCHAR(255), vencimiento DATE, etiquieta VARCHAR(255), estado VARCHAR(255))")
    cursor.execute("USE Tareas")
except Exception as ex:
    print(ex)