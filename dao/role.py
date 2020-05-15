import mysql.connector
from mysql.connector import Error
from config.localConfig import mysql as config

class RoleDao:
    
    def __init__(self):
        super().__init__()

        self.connection = mysql.connector.connect(**config)

    def orderBy(self, attribute):
        if attribute == 'rid':
            return "order by role_id "
        elif attribute == 'rname':
            return "order by role_name "
        else:
            return ""
    
    def getAllRoles(self, limit = 25, offset = 0, orderBy = 'rid'):
        cursor = self.connection.cursor()
        query = ("select * from roles ")
        query += self.orderBy(orderBy)
        query += ("limit %s offset %s ")
        cursor.execute(query, (limit, offset))
        result = cursor.fetchall()
        cursor.close()
        return result
    
    def getRoleById(self, roleID):
        cursor = self.connection.cursor()
        query = ("select * from roles where role_id = %s ")
        cursor.execute(query, (roleID,))
        result = cursor.fetchone()
        cursor.close()
        return result
    
    def getRoleByName(self, roleName):
        cursor = self.connection.cursor()
        query = ("select * from roles where role_name = %s ")
        cursor.execute(query, (roleName,))
        result = cursor.fetchone()
        cursor.close()
        return result

    def getRoleByUser(self, userID):
        cursor = self.connection.cursor()
        query = ("select * from users natural join roles "
        "where user_id = %s ")
        cursor.execute(query, (userID,))
        result = cursor.fetchone()
        cursor.close()
        return result


    def insert(self, name):
        cursor = self.connection.cursor()
        inserQuery = ("insert into roles(role_name) "
        "values (%s) ")
        cursor.execute(inserQuery, (name,))
        rID = cursor.lastrowid
        self.connection.commit()
        cursor.close()
        return rID