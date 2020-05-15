import mysql.connector
from mysql.connector import Error
from config.localConfig import mysql as config

class CategoryDao:

    def __init__(self):
        super().__init__()

        self.connection = mysql.connector.connect(**config)
    
    def orderBy(self, attribute):
        if attribute == 'cid':
            return "order by category_id "
        elif attribute == "name":
            return "order by category_name "
        elif attribute == "parent":
            return "order by parent_category "
        else:
            return ""

    def getAllCategories(self, limit = 25, offset = 0, orderBy = 'cid'):
        cursor = self.connection.cursor()
        query = ("select * from categories ")
        query += self.orderBy(orderBy)
        query += ("limit %s offset %s ")
        cursor.execute(query, (limit, offset))
        result = cursor.fetchall()
        cursor.close()
        return result

    def getCategoryByID(self, categoryID):
        cursor = self.connection.cursor()
        query = ("select * from categories where category_id = %s ")
        cursor.execute(query, (categoryID,))
        result = cursor.fetchone()
        cursor.close()
        return result

    def getCategoryByName(self, categoryName):
        cursor = self.connection.cursor()
        query = ("select * from categories where category_name = %s ")
        cursor.execute(query, (categoryName,))
        result = cursor.fetchone()
        cursor.close()
        return result

    def getCategoriesByParent(self, parentCategory, limit = 25, offset = 0, orderBy = 'cid'):
        cursor = self.connection.cursor()
        query = ("select * from categories where category_id = %s "
        "or parent_category = %s ")
        query += self.orderBy(orderBy)
        query += ("limit %s offset %s ")
        cursor.execute(query, (parentCategory, parentCategory, limit, offset))
        result = cursor.fetchall()
        cursor.close()
        return result

    def getParentByCategory(self, categoryID):
        cursor = self.connection.cursor()
        query = ("select * from categories where category_id in "
        "(select parent_category from categories where category_id = %s) ")
        cursor.execute(query, (categoryID,))
        result = cursor.fetchone()
        cursor.close()
        return result

    def getCategoryByResource(self, resourceID):
        cursor = self.connection.cursor()
        query = ("select * from resources natural join categories "
        "where resource_id = %s ")
        cursor.execute(query, (resourceID,))
        result = cursor.fetchone()
        cursor.close()
        return result


    def insert(self, name, parent):
        cursor = self.connection.cursor()
        inserQuery = ("insert into categories(category_name, parent_category) "
        "values (%s, %s) ")
        cursor.execute(inserQuery, (name, parent))
        userId = cursor.lastrowid
        self.connection.commit()
        cursor.close()
        return userId