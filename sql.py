Python 3.8.7 (tags/v3.8.7:6503f05, Dec 21 2020, 17:59:51) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user ="root",
    password="",
    port=3306


)
mycursor = mydb.cursor()

mycursor.execute("create database komal")
print("database created")