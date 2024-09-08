from tareas import *
from users import *

def main():

    while True:
        solicitud = input("Selecciona una opción (1 para login, 2 para registro): ")
        
        if solicitud == '1':
            while True:
                username = input("NOMBRE DE USUARIO: ")
                password = input("CONTRASEÑA: ")
                authentication = Login(username, password)
                if authentication:
                    print("Inicio de sesión exitoso")
                    break
                else:
                    print("Usuario o Contraseña equivocada, intenta de nuevo.")
            break
        elif solicitud == '2':
            username = input("NOMBRE DE USUARIO: ")
            password = input("CONTRASEÑA: ")
            Register(username,password)
        else:
            print("Selecciona un número correcto (1 o 2). Inténtalo de nuevo.")

    if authentication:
        print("HOLAAAAAAAA")
    else:
        print("MALARDIUM")



if __name__ == "__main__":
    main()