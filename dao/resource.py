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
        elif attribute == 'priceDESC':
            return "order by price desc "
        elif attribute == 'priceASC':
            return "order by price asc "
        elif attribute == 'stock':
            return "order by stock desc "
        else:
            return ""

    def getAllResources(self, minStock = 0, minPrice = 0, maxPrice = 9999999999999.99, limit = 25, offset = 0, orderBy = 'name'):
        cursor = self.connection.cursor()
        query = ("select * from resources natural join categories natural join addresses natural join senate_region "
                "where stock >= %s and price between %s and %s ")
        query += self.orderBy(orderBy)
        query += ("limit %s offset %s ")

        cursor.execute(query, (minStock, minPrice, maxPrice, limit, offset))
        result = cursor.fetchall()
        cursor.close()
        return result
    
    def getAllRequestedResources(self, minStock = 0, minPrice = 0, maxPrice = 9999999999999.99, limit = 25, offset = 0, orderBy = 'name'):
        cursor = self.connection.cursor()
        query = ("select * from resources natural join categories natural join addresses natural join senate_region "
                "inner join requests on resources.resource_id=requests.resource_id "
                "where stock >= %s and price between %s and %s ")
        query += self.orderBy(orderBy)
        query += ("limit %s offset %s ")

        cursor.execute(query, (minStock, minPrice, maxPrice, limit, offset))
        result = cursor.fetchall()
        cursor.close()
        return result

    def getAllUnrequestedResources(self, minStock = 0, minPrice = 0, maxPrice = 9999999999999.99, limit = 25, offset = 0, orderBy = 'name'):
        cursor = self.connection.cursor()
        query = ("select * from resources natural join categories natural join addresses natural join senate_region "
                "where stock >= %s and price between %s and %s "
                "and resource_id not in (select resource_id from resources natural join requests)")
        query += self.orderBy(orderBy)
        query += ("limit %s offset %s ")

        cursor.execute(query, (minStock, minPrice, maxPrice, limit, offset))
        result = cursor.fetchall()
        cursor.close()
        return result

    def getResourceById(self, resourceId):
        cursor = self.connection.cursor()
        query = ("select * from resources natural join categories natural join addresses natural join senate_region "
                "where resource_id = %s ")

        cursor.execute(query, (resourceId,))
        result = cursor.fetchone()
        cursor.close()
        return result

    def getResourcesBySupplier(self, supplierId, minStock = 0, minPrice = 0, maxPrice = 9999999999999.99, limit = 25, offset = 0, orderBy = 'name'):
        cursor = self.connection.cursor()
        query = ("select * from resources natural join categories natural join addresses natural join senate_region "
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
                "select category_id, parent_category from categories where category_id=%s "
                "union all "
                "select c.category_id, c.parent_category from category_tree as ct inner join categories as c on ct.category_id=c.parent_category "
                ") "
                "select * "
                "from resources natural join categories natural join addresses natural join senate_region "
                "where stock >= %s and price between %s and %s and category_id in (select category_id from category_tree) ")
        query += self.orderBy(orderBy)
        query += ("limit %s offset %s ")

        cursor.execute(query, (categoryId, minStock, minPrice, maxPrice, limit, offset))
        result = cursor.fetchall()
        cursor.close()
        return result

    def getResourcesBySenateRegion(self, regionId, minStock = 0, minPrice = 0, maxPrice = 9999999999999.99, limit = 25, offset = 0, orderBy = 'name'):
        cursor = self.connection.cursor()
        query = ("select * "
                "from resources natural join categories natural join addresses natural join senate_region "
                "where region_id=%s and stock >= %s and price between %s and %s ")
        query += self.orderBy(orderBy)
        query += ("limit %s offset %s ")

        cursor.execute(query, (regionId, minStock, minPrice, maxPrice, limit, offset))
        result = cursor.fetchall()
        cursor.close()
        return result

    def getResourcesByCategoryAndSenateRegion(self, categoryId, regionId, minStock = 0, minPrice = 0, maxPrice = 9999999999999.99, limit = 25, offset = 0, orderBy = 'name'):
        cursor = self.connection.cursor()
        query = ("with recursive "
                "category_tree(category_id, parent_category) as "
                "( "
                "select category_id, parent_category from categories where category_id=%s "
                "union all "
                "select c.category_id, c.parent_category from category_tree as ct inner join categories as c on ct.category_id=c.parent_category "
                ") "
                "select * "
                "from resources natural join categories natural join addresses natural join senate_region "
                "where region_id=%s and stock >= %s and price between %s and %s and category_id in (select category_id from category_tree) ")
        query += self.orderBy(orderBy)
        query += ("limit %s offset %s ")

        cursor.execute(query, (categoryId, regionId, minStock, minPrice, maxPrice, limit, offset))
        result = cursor.fetchall()
        cursor.close()
        return result

    def getResourcesByCategoryAndSupplier(self, categoryId, supplierId, minStock = 0, minPrice = 0, maxPrice = 9999999999999.99, limit = 25, offset = 0, orderBy = 'name'):
        cursor = self.connection.cursor()
        query = ("with recursive "
                "category_tree(category_id, parent_category) as "
                "( "
                "select category_id, parent_category from categories where category_id=%s "
                "union all "
                "select c.category_id, c.parent_category from category_tree as ct inner join categories as c on ct.category_id=c.parent_category "
                ") "
                "select * "
                "from resources natural join categories natural join addresses natural join senate_region "
                "where user_id=%s and stock >= %s and price between %s and %s and category_id in (select category_id from category_tree) ")
        query += self.orderBy(orderBy)
        query += ("limit %s offset %s ")

        cursor.execute(query, (categoryId, supplierId, minStock, minPrice, maxPrice, limit, offset))
        result = cursor.fetchall()
        cursor.close()
        return result
    
    def getResourcesByKeywords(self, keywords, minStock = 0, minPrice = 0, maxPrice = 9999999999999.99, limit = 25, offset = 0, orderBy = 'name'):
        cursor = self.connection.cursor()
        query = ("select * "
                "from resources natural join categories natural join addresses natural join senate_region "
                "where stock >= %s and price between %s and %s "
                "and (match(resource_name, description) against (%s) or "
                "match(category_name) against (%s)) ")
        query += self.orderBy(orderBy)
        query += ("limit %s offset %s ")

        cursor.execute(query, (minStock, minPrice, maxPrice, keywords, keywords, limit, offset))
        result = cursor.fetchall()
        cursor.close()
        return result
