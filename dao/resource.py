import mysql.connector
from mysql.connector import Error
from config.localConfig import mysql as config

# connection = mysql.connector.connect(**config)

class ResourceDao:

    def __init__(self):
        super().__init__()

        self.connection = mysql.connector.connect(**config)
    
    def orderBy(self, attribute):

        if attribute == 'name':
            return "order by resource_name "
        elif attribute == 'description':
            return "order by description "
        elif attribute == 'price':
            return "order by price "
        elif attribute == 'stock':
            return "order by stock "
        else:
            return ""

    def getAllResources(self, minStock = 0, minPrice = 0, maxPrice = 9999999999999.99, limit = 25, offset = 0, orderBy = 'name'):
        cursor = self.connection.cursor()
        query = ("select * from resources natural join addresses "
                "where stock >= %s and price between %s and %s ")
        query += self.orderBy(orderBy)
        query += ("limit %s offset %s ")

        cursor.execute(query, (minStock, minPrice, maxPrice, limit, offset))
        result = cursor.fetchall()
        cursor.close()
        return result

    def getResourceById(self, resourceId):
        cursor = self.connection.cursor()
        query = ("select * from resources natural join addresses "
                "where resource_id = %s ")

        cursor.execute(query, (resourceId,))
        result = cursor.fetchone()
        cursor.close()
        return result

    def getResourcesBySupplier(self, supplierId, minStock = 0, minPrice = 0, maxPrice = 9999999999999.99, limit = 25, offset = 0, orderBy = 'name'):
        cursor = self.connection.cursor()
        query = ("select * from resources natural join addresses "
                "where user_id=%s and stock >= %s and price between %s and %s ")
        query += self.orderBy(orderBy)
        query += ("limit %s offset %s ")

        cursor.execute(query, (supplierId, minStock, minPrice, maxPrice, limit, offset))
        result = cursor.fetchall()
        cursor.close()
        return result

    def getResourcesByCategory(self, categoryId, minStock = 0, minPrice = 0, maxPrice = 9999999999999.99, limit = 25, offset = 0, orderBy = 'name'):
        cursor = self.connection.cursor()
        query = ("with recursive "
                "category_tree(category_id, parent_category) as "
                "( "
                "select category_id, parent_category from categories where parent_category=%s "
                "union all "
                "select c.category_id, c.parent_category from category_tree as ct inner join categories as c on ct.category_id=c.parent_category "
                ") "
                "select resources.*, category_name "
                "from resources natural join categories natural join addresses "
                "where stock >= %s and price between %s and %s and category_id in (select category_id from category_tree) ")
        query += self.orderBy(orderBy)
        query += ("limit %s offset %s ")

        cursor.execute(query, (categoryId, minStock, minPrice, maxPrice, limit, offset))
        result = cursor.fetchall()
        cursor.close()
        return result

    def getRecourcesBySenateRegion(self, senateRegion, minStock = 0, minPrice = 0, maxPrice = 9999999999999.99, limit = 25, offset = 0, orderBy = 'name'):
        cursor = self.connection.cursor()
        query = ("select * "
                "from resources natural join addresses "
                "where senate_region=%s and stock >= %s and price between %s and %s ")
        query += self.orderBy(orderBy)
        query += ("limit %s offset %s ")

        cursor.execute(query, (senateRegion, minStock, minPrice, maxPrice, limit, offset))
        result = cursor.fetchall()
        cursor.close()
        return result

print(ResourceDao().getResourcesBySupplier(supplierId=1))
