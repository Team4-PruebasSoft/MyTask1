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
            menu = int(input("Selecciona una opción (1 para crear una tarea, 2 para consultar una tarea, 3 para actualizar una tarea, 4 para eliminar una tarea, 5 para salir): "))

            if menu == 1:
                title = input("Titulo: ")
                description = input("Descripción: ")
                date = input("Fecha de vencimiento(YYYY-MM-DD): ")
                tag = input("Etiquieta: ")
                try:
                    fecha = datetime.datetime.strptime(date, "%Y-%m-%d").date()
                    print(fecha)
                except ValueError:
                    print("Formato de fecha incorrecto. Use el formato YYYY-MM-DD.")
                MakeIssue(title,description,fecha,tag)

            elif menu == 2:
                print("ACA SE DEBERIA PODER CONSULTAR")

            elif menu == 3:
                print("ACA SE DEBERIA ACTUALIZAR TAREA") # HAERLO POR ID

            elif menu == 4:

                print("ACA SE DEBERIA ELIMINAR TAREA") #HACER POR ID
            elif menu == 5:
                print("ADIOS")
                break
            
            else:
                print("NUMERO INCORRECTO")

if __name__ == "__main__":
    main()