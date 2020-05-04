import mysql.connector
from mysql.connector import Error
from config.localConfig import mysql as config

class RoleDao:
    def __init__(self):
        super().__init__()

        self.connection = mysql.connector.connect(**config)

    def orderBy(self, attribute):
        if attribute == 'rid':
            return "order by role_id"
        elif attribute == 'uid':
            return "order by user_id"
        elif attribute == 'name':
            return "order by name"
        else:
            return ""
    
    def getAllRoles(self, limit = 25, offset = 0, orderBy = 'rid'):
        cursor = self.connection.cursor()
        query = ("select * from roles")
        query += self.orderBy(orderBy)
        query += ("limit %s offset %s ")
        cursor.execute(query, (limit, offset))
        result = cursor.fetchall()
        cursor.close()
        return result
    
    def getRoleById(self, roleID):
        cursor = self.connection.cursor()
        query = ("select role_id, role_name from roles where role_id = %s")
        cursor.execute(query, roleID)
        result = cursor.fetchone()
        cursor.close()
        return result
    
    def getRoleByName(self, roleName):
        cursor = self.connection.cursor()
        query = ("select role_name, role_id from roles where role_name = %s")
        cursor.execute(query, roleName)
        result = cursor.fetchone()
        cursor.close()
        return result
