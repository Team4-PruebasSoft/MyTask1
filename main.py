from tareas import *
from users import *
import datetime
import logging 
import logger_config

def main():
    logging.info("Iniciando la aplicación.")
    MakeUsersBD()
    while True:
        solicitud = input("Selecciona una opción (1 para login, 2 para registro): ")
        if solicitud == '1':
            logging.info("Ingreso a la opción de inicio de sesión.")
            username = input("NOMBRE DE USUARIO: ") 
            password = input("CONTRASEÑA: ")
            authentication = Login(username, password)
            if authentication:
                logging.info("Inicio de sesión exitoso.")
                print("Inicio de sesión exitoso")
                break
            else: 
                logging.warning("Inicio de sesión fallada. Usiario no encontrado.")
                print("Usuario o Contraseña equivocada, intenta de nuevo.")
        elif solicitud == '2': 
            logging.info("Ingreso a la opción de registro.") 
            username = input("NOMBRE DE USUARIO: ")
            while username == "":
                logging.warning("Nombre de usuario vacío en el registro.")
                print("Nombre de usuario no puede estar vacío.")
                username = input("NOMBRE DE USUARIO: ")
            password = input("CONTRASEÑA: ")
            while password == "":
                logging.warning("Contraseña vacía en el registro.")
                print("Contraseña no puede estar vacía.")
                password = input("CONTRASEÑA: ")
            Register(username,password)
        else:
            print("Opción no válida, inténtelo de nuevo.") 
            logging.warning("Ingreso de opción no válida en el menú de inicio de sesión.")
    MakeTareasBD()
    UpdateExpiredIssues()
    if authentication:
        while True: 
            logging.info("Ingreso al menú de tareas.")
            menu = int(input("Selecciona una opción (1 para crear una tarea, 2 para ver las tareas, 3 para actualizar una tarea, 4 para eliminar una tarea, 5 para cambiar estado de una tarea, 6 para busqueda avanzada, 7 para salir): "))
            if menu == 1: 
                logging.info("Ingreso a la opción de creación de tareas.")
                title = input("Titulo: ")
                while title == "": 
                    logging.warning("Titulo vacío en la creación de tareas.")
                    print("El título no puede estar vacío.")
                    title = input("Titulo: ")
                description = input("Descripción: ")
                while description == "":
                    logging.warning("Descripción vacía en la creación de tareas.")
                    print("La descripción no puede estar vacía.")
                    description = input("Descripción: ")
                date = input("Fecha de vencimiento(YYYY-MM-DD): ")
                while date == "":
                    logging.warning("Fecha de vencimiento vacía en la creación de tareas.")
                    print("La fecha no puede estar vacía.")
                    date = input("Fecha de vencimiento(YYYY-MM-DD): ")
                tag = input("Etiqueta: ")
                while tag == "":
                    logging.warning("Etiqueta vacía en la creación de tareas.")
                    print("La etiqueta no puede estar vacía.")
                    tag = input("Etiqueta: ")
                try:
                    fecha = datetime.datetime.strptime(date, "%Y-%m-%d").date()
                    MakeIssue(title,description,fecha,tag)
                except ValueError: 
                    logging.warning("Formato de fecha usado incorrecto.")
                    print("Formato de fecha incorrecto. Use el formato YYYY-MM-DD.")
            elif menu == 2: 
                logging.info("Ingreso a la opción de visualización de tareas.")
                ViewIssue()
            elif menu == 3: 
                logging.info("Ingreso a la opción de actualización de tareas.")
                id_issue = int(input("Ingresa el ID del Issue a modificar: "))
                while True:
                    select = int(input("Selecciona una opcion(1 Titulo, 2 Descripción, 3 Fecha Vencimiento, 4 Tag, 5 Salir): "))
                    if select == 1: 
                        logging.info("Ingreso a la opción de actualización de título de tareas.")
                        title = input("Ingresa el nuevo titulo: ")
                        UpdateIssueTitle(id_issue,title)
                    elif select == 2:
                        logging.info("Ingreso a la opción de actualización de descripción de tareas.")
                        desc = input("Ingresa nueva descripción: ")
                        UpdateIssueDesc(id_issue,desc)
                    elif select == 3:
                        logging.info("Ingreso a la opción de actualización de fecha de vencimiento de tareas.")
                        fecha = input("Ingresa nueva fecha de vencimiento(YYYY-MM-DD): ")
                        try:
                            format_fecha = datetime.datetime.strptime(fecha, "%Y-%m-%d").date()
                        except ValueError:
                            logging.warning("Formato de fecha usado incorrecto en actualización de fecha de vencimiento de tareas.")
                            print("Formato de fecha incorrecto. Use el formato YYYY-MM-DD.")
                        UpdateIssueDate(id_issue,format_fecha)
                    elif select == 4: 
                        logging.info("Ingreso a la opción de actualización de etiqueta de tareas.")
                        tag = input("Ingresa el nuevo Tag: ")
                        UpdateIssueTag(id_issue,tag)
                    elif select == 5:
                        logging.info("Salida de la opción de actualización de tareas.")
                        break
                    else:
                        logging.warning("Ingreso de opción no válida en el menú de actualización de tareas.")
                        print("NUMERO INCORRECTO")
            elif menu == 4:
                logging.info("Ingreso a la opción de eliminación de tareas.")
                id_issue = int(input("Ingresa el ID de la tarea que deseas eliminar: "))
                DeleteIssue(id_issue)
            elif menu == 5:
                logging.info("Ingreso a la opción de cambio de estado de tareas.")
                while True: 
                        user_input = input("Ingresa el ID del Issue a modificar: ")
                        if user_input.isdigit():
                            id_issue = int(user_input)
                            break
                        else: 
                            print("Por favor, ingresa un número válido.") 
                            logging.warning("Ingreso de ID de tarea no válido en cambio de estado de tareas.")
                new_status = input("Ingresa el estado nuevo de la tarea: ") 
                while new_status not in ["pendiente", "en progreso", "completada"]:
                    print("Estado no válido. Por favor, ingresa un estado válido.")
                    logging.warning("Ingreso de estado no válido en cambio de estado de tareas.")
                    new_status = input("Ingresa el estado nuevo de la tarea: ")
                UpdateIssueStatus(id_issue,new_status)
            elif menu == 6:
                logging.info("Ingreso a la opción de búsqueda avanzada.")
                while True:
                    filter_option = int(input("Selecciona una opción para filtrar las tareas (1 para filtrar por título, 2 por estado, 3 por etiqueta, 4 por rango de fechas, 5 para salir): "))
                    if filter_option == 1: 
                        logging.info("Ingreso a la opción de filtrar por título.")
                        title = input("Ingrese el título de la tarea a buscar: ")
                        FilterIssuesByTitle(title)
                    elif filter_option == 2:
                        logging.info("Ingreso a la opción de filtrar por estado.")
                        status = input("Ingrese el estado de la tarea (pendiente, en progreso, completada): ")
                        FilterIssuesByStatus(status)
                    elif filter_option == 3:
                        logging.info("Ingreso a la opción de filtrar por etiqueta.")
                        tag = input("Ingrese la etiqueta: ")
                        FilterIssuesByTag(tag)
                    elif filter_option == 4: 
                        logging.info("Ingreso a la opción de filtrar por rango de fechas.")
                        start_date = input("Ingrese la fecha de inicio del rango (YYYY-MM-DD): ")
                        end_date = input("Ingrese la fecha de fin del rango (YYYY-MM-DD): ")
                        try:
                            format_start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d").date()
                            format_end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d").date()
                            FilterIssuesByDateRange(format_start_date, format_end_date)
                        except ValueError:
                            logging.warning("Formato de fecha usado incorrecto en filtrado por rango de fechas.")
                            print("Formato de fecha incorrecto. Use el formato YYYY-MM-DD.")
                    elif filter_option == 5:
                        logging.info("Salida de la opción de búsqueda avanzada.")
                        break
                    else:
                        logging.warning("Ingreso de opción no válida en el menú de búsqueda avanzada.")
                        print("Opción no válida, inténtelo de nuevo.")

            elif menu == 7: 
                logging.info("Salida de la aplicación.")
                print("ADIOS")
                break
            else: 
                logging.warning("Ingreso de opción no válida en el menú de tareas.")
                print("Opción no válida, inténtelo de nuevo.")

if __name__ == "__main__":
    main()