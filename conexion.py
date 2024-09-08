import pyodbc

try:
    connection = pyodbc.connect("DRIVER={SQL SERVER}; SERVER=KuVe-PC\SQLEXPRESS;Trusted_Connection=yes", autocommit=True)
    cursor = connection.cursor()
except Exception as ex:
    print(ex)
