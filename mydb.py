import mysql.connector

DataBase = mysql.connector.connect(
    host = 'localhost',
    user =  'root',
    password = '1017'
)

cursorObject = DataBase.cursor()

cursorObject.execute('CREATE DATABASE my_db')


print("ALL DONE") 