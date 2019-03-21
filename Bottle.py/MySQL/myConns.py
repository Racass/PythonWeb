import mysql.connector

def getMySQLConn() -> mysql.connector.connection.MySQLConnection:
    mydb = mysql.connector.connect(
        host="192.168.1.41",
        user="rafael",
        passwd="rafael36",
        database="PythonTests"
    )
    return mydb
