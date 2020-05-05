import mysql.connector
from mysql.connector import Error
from config.localConfig import mysql as config

# handled in resourceHandler, may need to add stuff there
class RequestDao:

    def __init__(self):
        super().__init__()

        self.connection = mysql.connector.connect(**config)

    def orderBy(self, attribute):
        if attribute == "ResName":
            return "order by resource_name "
        elif attribute == "ReqID":
            return "order by request_id "
        else:
            return ""

    def getAllRequests(self, limit = 25, offset = 0, orderBy = 'ReqID'):
        cursor = self.connection.cursor()
        query = ("select * from requests natural join users natural join resources ")
        query += self.orderBy(orderBy)
        query += ("limit %s offset %s ")
        cursor.execute(query, (limit, offset))
        result = cursor.fetchall()
        cursor.close()
        return result

    def getRequestByID(self, reqid):
        cursor = self.connection.cursor()
        query = ("select * from requests natural join users natural join resources "
        "where request_id = %s ")
        cursor.execute(query, reqid)
        result = cursor.fetchone()
        cursor.close()
        return result

    def getAllUnsatisfiedRequests(self, limit = 25, offset = 0, orderBy = 'ReqID'):
        cursor = self.connection.cursor()
        query = ("select * from requests natural join users natural join resources "
        "where is_satisfied = 0 ")
        query += self.orderBy(orderBy)
        query += "limit %s offset %s "
        cursor.execute(query, (limit, offset))
        result = cursor.fetchall()
        cursor.close()
        return result

    def getAllSatisfiedRequests(self, limit = 25, offset = 0, orderBy = 'ReqID'):
        cursor = self.connection.cursor()
        query = ("select * from requests natural join users natural join resources "
        "where is_satisfied = 1 ")
        query += self.orderBy(orderBy)
        query += "limit %s offset %s "
        cursor.execute(query, (limit, offset))
        result = cursor.fetchall()
        cursor.close()
        return result

    def getRequestsByDate(self, date, limit = 25, offset = 0, orderBy = "ReqID"):
        cursor = self.connection.cursor()
        query = ("select * from requests natural join users natural join resources "
        "where date = %s ")
        query += self.orderBy(orderBy)
        query += "limit %s offset %s "
        cursor.execute(query, (date, limit, offset))
        result = cursor.fetchall()
        cursor.close()
        return result

    def getRequestsByUserID(self, uid, limit = 25, offset = 0, orderBy = "ReqID"):
        cursor = self.connection.cursor()
        query = ("select * from requests natural join users natural join resources "
        "where user_id = %s ")
        query += self.orderBy(orderBy)
        query += "limit %s offset %s "
        cursor.execute(query, (uid, limit, offset))
        result = cursor.fetchall
        cursor.close()
        return result

    def getRequestsByResourceID(self, rid, limit = 25, offset = 0, orderBy = "ReqID"):
        cursor = self.connection.cursor()
        query = ("select * form requests natural join users natural join resources "
        "where resource_id = %s ")
        query += self.orderBy(orderBy)
        query += "limit %s offset %s "
        cursor.execute(query, (rid, limit, offset))
        result = cursor.fetchall()
        cursor.close()
        return result

    # assuming only one is possible. If many, add things that make it fetch all.
    def getRequestByUserIDAndResourceID(self, uid, resid, limit = 25, offset = 0, orderBy = 'ReqID'):
        cursor = self.connection.cursor()
        query = ("select * from requests natural join users natural join resources "
        "where user_id = %s and resource_id = %s ")
        query += self.orderBy(orderBy)
        query += "limit %s offset %s "
        cursor.execute(query, (uid, resid, limit, offset))
        result = cursor.fetchall()
        cursor.close()
        return result

    def getRequestsByResourceName(self, rname, limit = 25, offset = 0, orderBy = "ResName"):
        cursor = self.connection.cursor()
        query = ("select * from requests natural join users natural join resources "
        "where resource_name = %s ")
        query += self.orderBy(orderBy)
        query += "limit %s offset %s " 
        cursor.execute(query, (rname, limit, offset))
        result = cursor.fetchall()
        cursor.close()
        return result
