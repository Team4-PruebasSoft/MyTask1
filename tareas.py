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

def ViewIssue():
    cursor.execute("SELECT * FROM issues")
    result = cursor.fetchall()
    if len(result) != 0:
        print("Tareas:")
        for i in result:
            print(f"id_tarea: {i[0]}: Titulo: {i[1]}, Descripción: {i[2]}, Fecha de Vencimiento: {i[3]}, Etiquieta: {i[4]}, Estado: {i[5]}.")  
    else:
        print("No tienes tareas")

def UpdateIssueTitle(id_issue,name):
    cursor.execute("UPDATE issues SET titulo=? WHERE id_tarea =?", name, id_issue)

def UpdateIssueDesc(id_issue,desc):
    cursor.execute("UPDATE issues SET descripcion=? WHERE id_tarea =?", desc, id_issue)

def UpdateIssueDate(id_issue,date):
    fecha = date.strftime("%Y-%m-%d")
    cursor.execute("UPDATE issues SET vencimiento=? WHERE id_tarea =?", fecha, id_issue)

def UpdateIssueTag(id_issue,tag):
    cursor.execute("UPDATE issues SET etiqueta=? WHERE id_tarea =?", tag, id_issue)

def DeleteIssue(id_issue):
    cursor.execute("SELECT * FROM issues WHERE id_tarea=?",id_issue)
    result = cursor.fetchone()
    if result is not None:
        cursor.execute("DELETE FROM issues WHERE id_tarea=?", id_issue)
        print("LA TAREA FUE ELIMINADA CON EXITO")
    else:
        print("La tarea con ese ID no existe")

def UpdateIssueStatus(id_issue,new_status):
    cursor.execute("UPDATE issues SET estado=? WHERE id_tarea =?", new_status, id_issue)