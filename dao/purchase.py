import mysql.connector
from mysql.connector import Error
from config.localConfig import mysql as config

# handled in resourceHandler, may need to add stuff there
class PurchaseDao:

    def __init__(self):
        super().__init__()

        self.connection = mysql.connector.connect(**config)

    def orderBy(self, attribute):
        if attribute == "ResName":
            return "order by resource_name "
        elif attribute == "PID":
            return "order by purchase_id "
        elif attribute == "priceDESC":
            return "order by price DESC "
        elif attribute == "priceASC":
            return "order by price "
        else:
            return ""

    def getAllPurchases(self, limit = 25, offset = 0, orderBy = 'PID'):
        cursor = self.connection.cursor()
        query = ("select * from purchases natural join resources ")
        query += self.orderBy(orderBy)
        query += ("limit %s offset %s ")
        cursor.execute(query, (limit, offset))
        result = cursor.fetchall()
        cursor.close()
        return result

    def getPurchaseByID(self, pid):
        cursor = self.connection.cursor()
        query = ("select * from purchases natural join resources "
        "where purchase_id = %s ")
        cursor.execute(query, (pid,))
        result = cursor.fetchone()
        cursor.close()
        return result

    def getPurchasesByDate(self, date, limit = 25, offset = 0, orderBy = "PID"):
        cursor = self.connection.cursor()
        query = ("select * from purchases natural join resources "
        "where date = %s ")
        query += self.orderBy(orderBy)
        query += "limit %s offset %s "
        cursor.execute(query, (date, limit, offset))
        result = cursor.fetchall()
        cursor.close()
        return result

    def getPurchasesByPrice(self, price, limit = 25, offset = 0, orderBy = "priceDESC"):
        cursor = self.connection.cursor()
        query = ("select * from purchases natural join resources "
        "where purchase_price = %s ")
        query += self.orderBy(orderBy)
        query += "limit %s offset %s "
        cursor.execute(query, (price, limit, offset))
        result = cursor.fetchall()
        cursor.close()
        return result

    def getPurchasesByUserID(self, uid, limit = 25, offset = 0, orderBy = "PID"):
        cursor = self.connection.cursor()
        query = ("select * from purchases natural join resources "
        "where purchases.user_id = %s ")
        query += self.orderBy(orderBy)
        query += "limit %s offset %s "
        cursor.execute(query, (uid, limit, offset))
        result = cursor.fetchall()
        cursor.close()
        return result

    def getPurchasesByResourceID(self, rid, limit = 25, offset = 0, orderBy = "PID"):
        cursor = self.connection.cursor()
        query = ("select * from purchases natural join resources "
        "where purchases.resource_id = %s ")
        query += self.orderBy(orderBy)
        query += "limit %s offset %s "
        cursor.execute(query, (rid, limit, offset))
        result = cursor.fetchall()
        cursor.close()
        return result

    def getPurchasesByUserIDAndResourceID(self, uid, resid, limit = 25, offset = 0, orderBy = 'PID'):
        cursor = self.connection.cursor()
        query = ("select * from purchases natural join resources "
        "where purchases.user_id = %s and purchases.resource_id = %s ")
        query += self.orderBy(orderBy)
        query += "limit %s offset %s "
        cursor.execute(query, (uid, resid, limit, offset))
        result = cursor.fetchall()
        cursor.close()
        return result

    def getPurchasesByResourceName(self, rname, limit = 25, offset = 0, orderBy = "ResName"):
        cursor = self.connection.cursor()
        query = ("select * from purchases natural join resources "
        "where resource_name = %s ")
        query += self.orderBy(orderBy)
        query += "limit %s offset %s " 
        cursor.execute(query, (rname, limit, offset))
        result = cursor.fetchall()
        cursor.close()
        return result
