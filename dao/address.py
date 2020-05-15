import mysql.connector
from mysql.connector import Error
from config.localConfig import mysql as config

class AddressDao:

    def __init__(self):
        super().__init__()

        self.connection = mysql.connector.connect(**config)

    def orderBy(self, attribute):
        if attribute == 'aid':
            return "order by address_id "
        elif attribute == 'street_address':
            return "order by street_address "
        elif attribute == 'city':
            return "order by city "
        elif attribute == 'country':
            return "order by country "
        elif attribute == 'zip_code':
            return "order by zip_code "
        elif attribute == 'region_id':
            return "order by region_id "
        else:
            return ""

    def getAllAddresses(self, limit = 25, offset = 0, orderBy = 'aid'):
        cursor = self.connection.cursor()
        query = ("select * from addresses ")
        query += self.orderBy(orderBy)
        query += ("limit %s offset %s ")
        cursor.execute(query, (limit, offset))
        result = cursor.fetchall()
        cursor.close()
        return result


    def getAddressById(self, adID):
        cursor = self.connection.cursor()
        query = ("select * from addresses where address_id = %s ")
        cursor.execute(query, (adID,))
        result = cursor.fetchone()
        cursor.close()
        return result


    def insert(self, street_address, city, country, zip_code, region_id, latitud, longitud, autoCommit = True):
        cursor = self.connection.cursor()
        inserQuery = ("insert into addresses(street_address, city, country, zip_code, region_id, latitud, longitud) "
        "values (%s, %s, %s, %s, %s, %s, %s) ")
        cursor.execute(inserQuery, (street_address, city, country, zip_code, region_id, latitud, longitud))
        addID = cursor.lastrowid
        if autoCommit:
            self.connection.commit()
        cursor.close()
        return addID


    def commit(self):
        self.connection.commit()


    def rollback(self):
        self.connection.rollback()
