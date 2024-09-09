import logging
import os

# Eliminar el archivo Logs.log si existe
log_file = "Logs.log"
if os.path.exists(log_file):
    os.remove(log_file)

# Configurar el logger
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename=log_file,
    filemode="a"
)