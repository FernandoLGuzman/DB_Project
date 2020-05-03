import mysql.connector
from mysql.connector import Error
from config.localConfig import mysql as config

class UserDao:

    def __init__(self):
        super().__init__()

        self.connection = mysql.connector.connect(**config)


    def orderBy(self, attribute):
        if attribute == 'First name':
            return "order by first_name "
        elif attribute == 'Last name':
            return "order by last_name "
        elif attribute == 'email':
            return "order by email "
        elif attribute == 'role':
            return "order by role_id "
        elif attribute == 'uid':
            return "order by user_id "
        else:
            return ""


    def getAllUsers(self, limit = 25, offset = 0, orderBy = 'uid'):
        cursor = self.connection.cursor()
        query = ("select * from users natural join roles natural join addresses ")
        query += self.orderBy(orderBy)
        query += ("limit %s offset %s ")
        cursor.execute(query, (limit, offset))
        result = cursor.fetchall()
        cursor.close()
        return result


    def getUserById(self, userID):
        cursor = self.connection.cursor()
        query = ("select * from users natural join roles natural join addresses "
        "where user_id = %s ")
        cursor.execute(query, (userID,))
        result = cursor.fetchone()
        cursor.close()
        return result