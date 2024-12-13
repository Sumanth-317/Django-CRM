import mysql.connector

dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Sumanth@317'
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE crmapp")

print("All Done!")
