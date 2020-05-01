import mysql.connector
from mysql.connector import Error
from config.localConfig import mysql as config

# connection = mysql.connector.connect(**config)

def getUser():
    connection = mysql.connector.connect(**config)
    query = "select * from user;"
    connection.execute(query)
    res = []
    for row in connection:
        res.append(row)
    return res 