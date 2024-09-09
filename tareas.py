import pyodbc
from conexion import cursor 
import logging
import logger_config
import datetime

def MakeTareasBD():
    try: 
        logging.info("Buscando base de datos llamada 'Tareas'.")
        cursor.execute("SELECT name FROM master.dbo.sysdatabases")
        bases = cursor.fetchall()
        base_list = []
        for i in bases:
            base_list.append(i[0])
        if "Tareas" not in base_list: 
            logging.info("Creando base de datos 'Tareas' ya que no se encuentra creada.")
            cursor.execute("CREATE DATABASE Tareas")
            cursor.execute("USE Tareas")
            cursor.execute("CREATE TABLE issues(id_tarea INT IDENTITY(1,1) PRIMARY KEY, titulo VARCHAR(255), descripcion VARCHAR(255), vencimiento DATE, etiqueta VARCHAR(255), estado VARCHAR(255))")
        cursor.execute("USE Tareas")
    except Exception as ex:
        logging.error(f"Error al buscar y/o crear la base de datos 'Tareas'.: {ex}")
        exit()

def MakeIssue(titulo,desc,date,tag): 
    fecha = date.strftime("%Y-%m-%d")
    issue_info = [titulo,desc,fecha,tag,"pendiente"] 
    try: 
        cursor.execute("INSERT INTO issues (titulo,descripcion,vencimiento,etiqueta,estado) VALUES (?,?,?,?,?)", issue_info) 
        print("TAREA AGREGADA CORRECTAMENTE") 
    except Exception as ex: 
        logging.error(f"Error al agregar la tarea: {ex}") 
        print("ERROR AL AGREGAR LA TAREA")
def ViewIssue(): 
    try:
        cursor.execute("SELECT * FROM issues")
        result = cursor.fetchall()
        if len(result) != 0:
            print("Tareas:")
            for i in result:
                print(f"id_tarea: {i[0]}: Titulo: {i[1]}, Descripción: {i[2]}, Fecha de Vencimiento: {i[3]}, Etiqueta: {i[4]}, Estado: {i[5]}.")  
        else:
            print("No tienes tareas")
    except Exception as ex:
        logging.error(f"Error al visualizar las tareas: {ex}")
        print("ERROR AL VISUALIZAR LAS TAREAS")
def UpdateIssueTitle(id_issue,name):  
    try: 
        cursor.execute("UPDATE issues SET titulo=? WHERE id_tarea =?", name, id_issue)
    except Exception as ex:
        logging.error(f"Error al actualizar el titulo de la tarea: {ex}")
        print("ERROR AL ACTUALIZAR EL TITULO DE LA TAREA")

def UpdateIssueDesc(id_issue,desc): 
    try:
        cursor.execute("UPDATE issues SET descripcion=? WHERE id_tarea =?", desc, id_issue) 
    except Exception as ex:
        logging.error(f"Error al actualizar la descripción de la tarea: {ex}")
        print("ERROR AL ACTUALIZAR LA DESCRIPCION DE LA TAREA")

def UpdateIssueDate(id_issue,date):
    fecha = date.strftime("%Y-%m-%d") 
    try:
        cursor.execute("UPDATE issues SET vencimiento=? WHERE id_tarea =?", fecha, id_issue)
    except Exception as ex:
        logging.error(f"Error al actualizar la fecha de vencimiento de la tarea: {ex}")
        print("ERROR AL ACTUALIZAR LA FECHA DE VENCIMIENTO DE LA TAREA")

def UpdateIssueTag(id_issue,tag): 
    try:
        cursor.execute("UPDATE issues SET etiqueta=? WHERE id_tarea =?", tag, id_issue)
    except Exception as ex:
        logging.error(f"Error al actualizar la etiqueta de la tarea: {ex}")
        print("ERROR AL ACTUALIZAR LA ETIQUETA DE LA TAREA")

def DeleteIssue(id_issue): 
    try:
        cursor.execute("SELECT * FROM issues WHERE id_tarea=?",id_issue)
        result = cursor.fetchone()
        if result is not None:
            cursor.execute("DELETE FROM issues WHERE id_tarea=?", id_issue)
            print("LA TAREA FUE ELIMINADA CON EXITO")
        else:
            print("La tarea con ese ID no existe") 
    except Exception as ex:
        logging.error(f"Error al eliminar la tarea: {ex}")
        print("ERROR AL ELIMINAR LA TAREA")

def UpdateIssueStatus(id_issue,new_status): 
    try:
        cursor.execute("UPDATE issues SET estado=? WHERE id_tarea =?", new_status, id_issue)
    except Exception as ex:
        logging.error(f"Error al actualizar el estado de la tarea: {ex}")
        print("ERROR AL ACTUALIZAR EL ESTADO DE LA TAREA")

def FilterIssuesByTitle(title): 
    try:
        cursor.execute("SELECT * FROM issues WHERE titulo LIKE ?", '%' + title + '%')
        result = cursor.fetchall()
        if result:
            for i in result:
                print(f"id_tarea: {i[0]}: Titulo: {i[1]}, Descripción: {i[2]}, Fecha de Vencimiento: {i[3]}, Etiqueta: {i[4]}, Estado: {i[5]}.")
        else:
            print(f"No se encontraron tareas con el título '{title}'")
    except Exception as ex:
        logging.error(f"Error al filtrar las tareas por título: {ex}")
        print("ERROR AL FILTRAR LAS TAREAS POR TITULO")

def FilterIssuesByStatus(status): 
    try:
        cursor.execute("SELECT * FROM issues WHERE estado=?", status)
        result = cursor.fetchall()
        if result:
            for i in result:
                print(f"id_tarea: {i[0]}: Titulo: {i[1]}, Descripción: {i[2]}, Fecha de Vencimiento: {i[3]}, Etiqueta: {i[4]}, Estado: {i[5]}.")
        else:
            print(f"No se encontraron tareas con estado '{status}'") 
    except Exception as ex:
        logging.error(f"Error al filtrar las tareas por estado: {ex}")
        print("ERROR AL FILTRAR LAS TAREAS POR ESTADO")

def FilterIssuesByTag(tag): 
    try:
        cursor.execute("SELECT * FROM issues WHERE etiqueta=?", tag)
        result = cursor.fetchall()
        if result:
            for i in result:
                print(f"id_tarea: {i[0]}: Titulo: {i[1]}, Descripción: {i[2]}, Fecha de Vencimiento: {i[3]}, Etiqueta: {i[4]}, Estado: {i[5]}.")
        else:
            print(f"No se encontraron tareas con la etiqueta '{tag}'")
    except Exception as ex:
        logging.error(f"Error al filtrar las tareas por etiqueta: {ex}")
        print("ERROR AL FILTRAR LAS TAREAS POR ETIQUETA")

def FilterIssuesByDateRange(start_date, end_date): 
    try:
        cursor.execute("SELECT * FROM issues WHERE vencimiento BETWEEN ? AND ?", start_date.strftime("%Y-%m-%d"), end_date.strftime("%Y-%m-%d"))
        result = cursor.fetchall()
        if result:
            for i in result:
                print(f"id_tarea: {i[0]}: Titulo: {i[1]}, Descripción: {i[2]}, Fecha de Vencimiento: {i[3]}, Etiqueta: {i[4]}, Estado: {i[5]}.")
        else:
            print(f"No se encontraron tareas entre las fechas '{start_date}' y '{end_date}'") 
    except Exception as ex:
        logging.error(f"Error al filtrar las tareas por rango de fechas: {ex}")
        print("ERROR AL FILTRAR LAS TAREAS POR RANGO DE FECHAS")

def UpdateExpiredIssues():
    try:
        current_date = datetime.date.today().strftime("%Y-%m-%d")
        cursor.execute("SELECT id_tarea, vencimiento FROM issues WHERE (estado = 'pendiente' OR estado = 'en progreso') AND vencimiento < ?", current_date)
        expired_issues = cursor.fetchall()
        if expired_issues:
            for issue in expired_issues:
                cursor.execute("UPDATE issues SET estado = 'atrasado' WHERE id_tarea = ?", issue[0])
            print(f"Se actualizaron {len(expired_issues)} tarea(s) a 'atrasado'.")
        else:
            print("No hay tareas vencidas para actualizar.")
    except Exception as ex:
        logging.error(f"Error al actualizar el estado de la tarea EXPIRED: {ex}")
        print("ERROR AL ACTUALIZAR EL ESTADO DE LA TAREA EXPIRED")
