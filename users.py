import pyodbc

try:
    connection = pyodbc.connect("DRIVER={SQL SERVER}; SERVER=KuVe-PC\SQLEXPRESS;Trusted_Connection=yes", autocommit = True)
    cursor = connection.cursor()
    cursor.execute("SELECT name FROM master.dbo.sysdatabases")
    bases = cursor.fetchall()
    base_list = []
    for i in bases:
        base_list.append(i[0])
    if "Users" not in base_list:
        cursor.execute("CREATE DATABASE Users")
        cursor.execute("USE Users")
        cursor.execute("CREATE TABLE usuarios(user_id INT IDENTITY(1,1) PRIMARY KEY, username VARCHAR(255), password VARCHAR(255))")
    cursor.execute("USE Users")
except Exception as ex:
    print(ex)

def Register(user, password):
    userinfo = [user,password]
    cursor.execute("SELECT * FROM usuarios WHERE username=? AND password =?", userinfo)
    res = cursor.fetchone()
    if res is None:
        cursor.execute("INSERT INTO usuarios (username,password) VALUES (?,?)", userinfo)
        print("REGISTRO EXITOSO")
    else:
        print("USUARIO YA REGISTRADO")

def Login (user, password):
    userinfo = [user,password]
    cursor.execute("SELECT * FROM usuarios WHERE username=? AND password =?", userinfo)
    res = cursor.fetchone()
    if res is not None:
        return True