import mysql.connector
from mysql.connector import Error
from config.localConfig import mysql as config

class RegionsDao:
    
    def __init__(self):
        super().__init__()

        self.connection = mysql.connector.connect(**config)

    def orderBy(self, attribute):
        if attribute == 'rid':
            return "order by region_id "
        elif attribute == 'name':
            return "order by name "
        else:
            return ""
    
    def getAllRegions(self, limit = 25, offset = 0, orderBy = 'rid'):
        cursor = self.connection.cursor()
        query = ("select * from senate_region ")
        query += self.orderBy(orderBy)
        query += ("limit %s offset %s ")
        cursor.execute(query, (limit, offset))
        result = cursor.fetchall()
        cursor.close()
        return result
    
    def getRegionById(self, regionID):
        cursor = self.connection.cursor()
        query = ("select * from senate_region where region_id = %s ")
        cursor.execute(query, (regionID,))
        result = cursor.fetchone()
        cursor.close()
        return result
    
    def getRegionByName(self, regionName):
        cursor = self.connection.cursor()
        query = ("select * from senate_region where name = %s ")
        cursor.execute(query, (regionName,))
        result = cursor.fetchone()
        cursor.close()
        return result
