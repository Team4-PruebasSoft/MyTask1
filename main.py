from tareas import *
from users import *
import datetime

def main():

    MakeUsersBD()
    flag = True

    while True:
        solicitud = input("Selecciona una opción (1 para login, 2 para registro): ")
        
        if solicitud == '1':
            username = input("NOMBRE DE USUARIO: ")
            password = input("CONTRASEÑA: ")
            authentication = Login(username, password)
            if authentication:
                print("Inicio de sesión exitoso")
                break
            else:
                print("Usuario o Contraseña equivocada, intenta de nuevo.")
        elif solicitud == '2':
            username = input("NOMBRE DE USUARIO: ")
            password = input("CONTRASEÑA: ")
            Register(username,password)
        else:
            print("Selecciona un número correcto (1 o 2). Inténtalo de nuevo.")

    MakeTareasBD()
    if authentication:
        while True:
            menu = int(input("Selecciona una opción (1 para crear una tarea, 2 para ver las tareas, 3 para actualizar una tarea, 4 para eliminar una tarea, 5 para cambiar estado de una tarea, 6 para salir): "))

            if menu == 1:
                title = input("Titulo: ")
                description = input("Descripción: ")
                date = input("Fecha de vencimiento(YYYY-MM-DD): ")
                tag = input("Etiquieta: ")
                try:
                    fecha = datetime.datetime.strptime(date, "%Y-%m-%d").date()
                except ValueError:
                    print("Formato de fecha incorrecto. Use el formato YYYY-MM-DD.")
                MakeIssue(title,description,fecha,tag)

            elif menu == 2:
                ViewIssue()

            elif menu == 3:
                id_issue = int(input("Ingresa el ID del Issue a modificar: "))
                while True:
                    select = int(input("Selecciona una opcion(1 Titulo, 2 Descripción, 3 Fecha Vencimiento, 4 Tag, 5 Salir): "))
                    if select == 1:
                        title = input("Ingresa el nuevo titulo: ")
                        UpdateIssueTitle(id_issue,title)
                    elif select == 2:
                        desc = input("Ingresa nueva descripción: ")
                        UpdateIssueDesc(id_issue,desc)
                    elif select == 3:
                        fecha = input("Ingresa nueva fecha de vencimiento(YYYY-MM-DD): ")
                        try:
                            format_fecha = datetime.datetime.strptime(fecha, "%Y-%m-%d").date()
                        except ValueError:
                            print("Formato de fecha incorrecto. Use el formato YYYY-MM-DD.")
                        UpdateIssueDate(id_issue,format_fecha)
                    elif select == 4:
                        tag = input("Ingresa el nuevo Tag: ")
                        UpdateIssueTag(id_issue,tag)
                    elif select == 5:
                        break
                    else:
                        print("NUMERO INCORRECTO")

            elif menu == 4:
                id_issue = int(input("Ingresa el ID de la tarea que deseas eliminar: "))
                DeleteIssue(id_issue)

            elif menu == 5:
                id_issue = int(input("Ingresa el ID del Issue a modificar: "))
                new_status = input("Ingresa el estado nuevo de la tarea: ")
                UpdateIssueStatus(id_issue,new_status)


            elif menu == 6:
                print("ADIOS")
                break

            else:
                print("NUMERO INCORRECTO")

if __name__ == "__main__":
    main()