import mysql.connector
from mysql.connector import Error
from config.localConfig import mysql as config

class PaymentDao:

    def __init__(self):
        super().__init__()

        self.connection = mysql.connector.connect(**config)


    def orderBy(self, attribute):
        if attribute == 'pmid':
            return "order by payment_method_id "
        elif attribute == 'uid':
            return "order by user_id "
        elif attribute == 'type':
            return "order by type "
        else:
            return ""


    def getAllPaymentMethods(self, limit = 25, offset = 0, orderBy = 'pmid'):
        cursor = self.connection.cursor()
        query = ("select * from payment_methods ")
        query += self.orderBy(orderBy)
        query += ("limit %s offset %s ")
        cursor.execute(query, (limit, offset))
        result = cursor.fetchall()
        cursor.close()
        return result


    def getPaymentMethodById(self, pmID):
        cursor = self.connection.cursor()
        query = ("select * from payment_methods "
        "where payment_method_id = %s ")
        cursor.execute(query, (pmID,))
        result = cursor.fetchone()
        cursor.close()
        return result


    def getPaymentMethodsByUserId(self, UserID, orderBy = 'pmid'):
        cursor = self.connection.cursor()
        query = ("select * from payment_methods "
        "where user_id = %s ")
        query += self.orderBy(orderBy)
        cursor.execute(query, (UserID,))
        result = cursor.fetchall()
        cursor.close()
        return result