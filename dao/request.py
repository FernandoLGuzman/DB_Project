import mysql.connector
from mysql.connector import Error
from config.localConfig import mysql as config
from datetime import datetime

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
        query = ("select * from requests inner join resources using(resource_id) ")
        query += self.orderBy(orderBy)
        query += ("limit %s offset %s ")
        cursor.execute(query, (limit, offset))
        result = cursor.fetchall()
        cursor.close()
        return result

    def getRequestByID(self, reqid):
        cursor = self.connection.cursor()
        query = ("select * from requests inner join resources using(resource_id) "
        "where request_id = %s ")
        cursor.execute(query, (reqid,))
        result = cursor.fetchone()
        cursor.close()
        return result

    def getAllUnsatisfiedRequests(self, limit = 25, offset = 0, orderBy = 'ReqID'):
        cursor = self.connection.cursor()
        query = ("select * from requests inner join resources using(resource_id) "
        "where is_satisfied = 0 ")
        query += self.orderBy(orderBy)
        query += "limit %s offset %s "
        cursor.execute(query, (limit, offset))
        result = cursor.fetchall()
        cursor.close()
        return result

    def getAllSatisfiedRequests(self, limit = 25, offset = 0, orderBy = 'ReqID'):
        cursor = self.connection.cursor()
        query = ("select * from requests inner join resources using(resource_id) "
        "where is_satisfied = 1 ")
        query += self.orderBy(orderBy)
        query += "limit %s offset %s "
        cursor.execute(query, (limit, offset))
        result = cursor.fetchall()
        cursor.close()
        return result

    def getRequestsByDate(self, date, limit = 25, offset = 0, orderBy = "ReqID"):
        cursor = self.connection.cursor()
        query = ("select * from requests inner join resources using(resource_id) "
        "where date = %s ")
        query += self.orderBy(orderBy)
        query += "limit %s offset %s "
        cursor.execute(query, (date, limit, offset))
        result = cursor.fetchall()
        cursor.close()
        return result

    def getRequestsByUserID(self, uid, limit = 25, offset = 0, orderBy = "ReqID"):
        cursor = self.connection.cursor()
        query = ("select * from requests inner join resources using(resource_id) "
        "where requests.user_id = %s ")
        query += self.orderBy(orderBy)
        query += "limit %s offset %s "
        cursor.execute(query, (uid, limit, offset))
        result = cursor.fetchall()
        cursor.close()
        return result

    def getRequestsByResourceID(self, rid, limit = 25, offset = 0, orderBy = "ReqID"):
        cursor = self.connection.cursor()
        query = ("select * from requests inner join resources using(resource_id) "
        "where requests.resource_id = %s ")
        query += self.orderBy(orderBy)
        query += "limit %s offset %s "
        cursor.execute(query, (rid, limit, offset))
        result = cursor.fetchall()
        cursor.close()
        return result

    def getRequestsByUserIDAndResourceID(self, uid, resid, limit = 25, offset = 0, orderBy = 'ReqID'):
        cursor = self.connection.cursor()
        query = ("select * from requests inner join resources using(resource_id) "
        "where requests.user_id = %s and requests.resource_id = %s ")
        query += self.orderBy(orderBy)
        query += "limit %s offset %s "
        cursor.execute(query, (uid, resid, limit, offset))
        result = cursor.fetchall()
        cursor.close()
        return result

    def getRequestsByResourceName(self, rname, limit = 25, offset = 0, orderBy = "ResName"):
        cursor = self.connection.cursor()
        query = ("select * from requests inner join resources using(resource_id) "
        "where resource_name = %s ")
        query += self.orderBy(orderBy)
        query += "limit %s offset %s " 
        cursor.execute(query, (rname, limit, offset))
        result = cursor.fetchall()
        cursor.close()
        return result

    def insertRequest(self, uid, rid, qty):
        cursor = self.connection.cursor()
        insertQuery = ("insert into requests(user_id, resource_id, quantity, date, is_satisfied) "
            "values(%s, %s, %s, %s, %s) ")
        cursor.execute(insertQuery, (uid, rid, qty, datetime.now().date(), 0))
        requestID = cursor.lastrowid
        self.connection.commit()
        cursor.close()
        return requestID
