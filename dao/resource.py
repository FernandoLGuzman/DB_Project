import mysql.connector
from mysql.connector import Error
from config.localConfig import mysql as config

# connection = mysql.connector.connect(**config)

class ResourceDao:

    def __init__(self):
        super().__init__()

        self.connection = mysql.connector.connect(**config)

    def getAllResources(self, limit = 25, offset = 0, orderBy = 'name'):
        cursor = self.connection.cursor()
        query = ("select * from resources "
                "order by %s"
                "limit %s offset %s")

        cursor.execute(query, (orderBy, limit, offset))
        return cursor.fetchall()


print(ResourceDao().getAllResources())
