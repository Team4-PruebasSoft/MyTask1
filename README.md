# MyTask1 
Angelo Russu y Gonzalo Alarcon  

## Descripción

Esta es una aplicación de gestión de tareas simple diseñada para ser utilizada desde la línea de comandos. Los usuarios pueden crear, consultar, actualizar y eliminar tareas. Cada tarea incluye un título, una descripción, una fecha de vencimiento y etiquetas para facilitar la organización (por ejemplo, "urgente", "trabajo", "personal", etc.). Además, los usuarios pueden filtrar y buscar tareas según la fecha de vencimiento, etiquetas o el estado de la tarea (pendiente, en progreso, completada).

La aplicación también ofrece un sistema de autenticación que protege el acceso a los datos mediante un nombre de usuario y contraseña.

### Características principales:
- Crear, consultar, actualizar y eliminar tareas.
- Filtrar y buscar tareas por fecha de vencimiento, etiquetas o estado.
- Gestión de estados de las tareas (pendiente, en progreso, completada).
- Autenticación con nombre de usuario y contraseña.
- Archivo de tareas completadas.

## Instalación
1. Clona el repositorio:
```bash
    git clone https://github.com/Team4-PruebasSoft/MyTask1
    cd MyTask1 
``` 
2. Librerias: 
```bash 
    python -m pip install pyodbc 
    python -m pip install logging 
``` 
3. Consideraciones 
    Para este programa, se usa base de datos local con server sql management studio. Se debe tener descargado esta herramienta. 
    En conexiones.py, se debe cambiar el nombre del server:  
```bash  
        connection = pyodbc.connect("DRIVER={SQL SERVER}; SERVER="Tu server";Trusted_Connection=yes", autocommit=True) 
```  

## Como usar 
Ejecuta el archivo main.py y registrate.  


## Cómo contribuir

¡Gracias por considerar contribuir a este proyecto de Pruebas de software! Para contribuir, sigue estos pasos:

1. Haz un fork del repositorio.
   - Haz clic en el botón "Fork" en la parte superior derecha de esta página.

2. Crea una nueva rama para tu funcionalidad o corrección de errores:
```bash
   git checkout -b nombre-de-tu-rama 
```


## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Puedes consultar el archivo [LICENSE](./LICENSE) para más detalles.

