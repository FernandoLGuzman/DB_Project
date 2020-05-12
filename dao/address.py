import mysql.connector
from mysql.connector import Error
from config.localConfig import mysql as config

class AddressDao:

    def __init__(self):
        super().__init__()

        self.connection = mysql.connector.connect(**config)


    def insert(self, street_address, city, country, zip_code, region_id, latitud, longitud):
        cursor = self.connection.cursor()
        inserQuery = ("insert into addresses(street_address, city, country, zip_code, region_id, latitud, longitud) "
        "values (%s, %s, %s, %s, %s, %s, %s) ")
        cursor.execute(inserQuery, (street_address, city, country, zip_code, region_id, latitud, longitud))
        userId = cursor.lastrowid
        self.connection.commit()
        cursor.close()
        return userId
