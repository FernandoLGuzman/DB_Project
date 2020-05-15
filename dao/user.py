import mysql.connector
from mysql.connector import Error
from config.localConfig import mysql as config

class UserDao:

    def __init__(self):
        super().__init__()

        self.connection = mysql.connector.connect(**config)


    def orderBy(self, attribute):
        if attribute == 'firstName':
            return "order by first_name "
        elif attribute == 'lastName':
            return "order by last_name "
        elif attribute == 'email':
            return "order by email "
        elif attribute == 'role':
            return "order by role_id "
        elif attribute == 'uid':
            return "order by user_id "
        else:
            return ""


    def getAllUsers(self, limit = 25, offset = 0, orderBy = 'uid'):
        cursor = self.connection.cursor()
        query = ("select * from users natural join roles natural join addresses natural join senate_region ")
        query += self.orderBy(orderBy)
        query += ("limit %s offset %s ")
        cursor.execute(query, (limit, offset))
        result = cursor.fetchall()
        cursor.close()
        return result


    def getUserById(self, userID):
        cursor = self.connection.cursor()
        query = ("select * from users natural join roles natural join addresses natural join senate_region "
        "where user_id = %s ")
        cursor.execute(query, (userID,))
        result = cursor.fetchone()
        cursor.close()
        return result

    
    def loginUser(self, email, password):
        cursor = self.connection.cursor()
        query = ("select * from users natural join roles natural join addresses natural join senate_region "
        "where email = %s and password = %s")
        cursor.execute(query, (email, password))
        result = cursor.fetchone()
        cursor.close()
        return result


    def getUsersByRoleID(self, roleID, limit = 25, offset = 0, orderBy = 'uid'):
        cursor = self.connection.cursor()
        query = ("select * from users natural join roles natural join addresses natural join senate_region "
                "where role_id=%s ")
        query += self.orderBy(orderBy)
        query += ("limit %s offset %s ")

        cursor.execute(query, (roleID, limit, offset))
        result = cursor.fetchall()
        cursor.close()
        return result


    def getUsersByRoleName(self, roleName, limit = 25, offset = 0, orderBy = 'uid'):
        cursor = self.connection.cursor()
        query = ("select * from users natural join roles natural join addresses natural join senate_region "
                "where role_name=%s ")
        query += self.orderBy(orderBy)
        query += ("limit %s offset %s ")

        cursor.execute(query, (roleName, limit, offset))
        result = cursor.fetchall()
        cursor.close()
        return result


    def getUsersByFullName(self, fname, lname, limit = 25, offset = 0, orderBy = 'uid'):
        cursor = self.connection.cursor()
        query = ("select * from users natural join roles natural join addresses natural join senate_region "
                "where first_name=%s and last_name=%s ")
        query += self.orderBy(orderBy)
        query += ("limit %s offset %s ")

        cursor.execute(query, (fname, lname, limit, offset))
        result = cursor.fetchall()
        cursor.close()
        return result


    def getUsersByEmail(self, email, limit = 25, offset = 0, orderBy = 'uid'):
        cursor = self.connection.cursor()
        query = ("select * from users natural join roles natural join addresses natural join senate_region "
                "where email=%s ")
        query += self.orderBy(orderBy)
        query += ("limit %s offset %s ")

        cursor.execute(query, (email, limit, offset))
        result = cursor.fetchall()
        cursor.close()
        return result


    def getUsersByPhoneNumber(self, number, limit = 25, offset = 0, orderBy = 'uid'):
        cursor = self.connection.cursor()
        query = ("select * from users natural join roles natural join addresses natural join senate_region "
                "where phone_number=%s ")
        query += self.orderBy(orderBy)
        query += ("limit %s offset %s ")

        cursor.execute(query, (number, limit, offset))
        result = cursor.fetchall()
        cursor.close()
        return result

    def insert(self, first_name, last_name, email, password, role_id, address_id, phone_number, autoCommit= True):
        cursor = self.connection.cursor()
        inserQuery = ("insert into users(first_name, last_name, email, password, role_id, address_id, phone_number) "
        "values (%s, %s, %s, %s, %s, %s, %s) ")
        cursor.execute(inserQuery, (first_name, last_name, email, password, role_id, address_id, phone_number))
        userId = cursor.lastrowid
        
        if autoCommit:
            self.connection.commit()
        cursor.close()
        return userId


    def signupNoPayment(self, first_name, last_name, email, password, role_id, phone_number, street_address, city, country, zip_code, senate_region, latitud, longitud):
        cursor = self.connection.cursor()

        addQuery = ("insert into addresses(street_address, city, country, zip_code, region_id, latitud, longitud) "
        "values (%s, %s, %s, %s, %s, %s, %s) ")
        cursor.execute(addQuery, (street_address, city, country, zip_code, senate_region, latitud, longitud))
        adID = cursor.lastrowid

        userQuery = ("insert into users(first_name, last_name, email, password, role_id, address_id, phone_number) "
        "values (%s, %s, %s, %s, %s, %s, %s) ")
        cursor.execute(userQuery, (first_name, last_name, email, password, role_id, adID, phone_number))
        userId = cursor.lastrowid

        self.connection.commit()
        cursor.close()
        return adID, userId

    
    def signupWiPayment(self, first_name, last_name, email, password, role_id, phone_number, street_address, city, country, zip_code, senate_region, latitud, longitud, type, wallet):
        cursor = self.connection.cursor()

        addQuery = ("insert into addresses(street_address, city, country, zip_code, region_id, latitud, longitud) "
        "values (%s, %s, %s, %s, %s, %s, %s) ")
        cursor.execute(addQuery, (street_address, city, country, zip_code, senate_region, latitud, longitud))
        adID = cursor.lastrowid

        userQuery = ("insert into users(first_name, last_name, email, password, role_id, address_id, phone_number) "
        "values (%s, %s, %s, %s, %s, %s, %s) ")
        cursor.execute(userQuery, (first_name, last_name, email, password, role_id, adID, phone_number))
        userId = cursor.lastrowid

        payQuery = ("insert into payment_methods(user_id, type, wallet) "
        "values (%s, %s, %s) ")
        cursor.execute(payQuery, (userId, type, wallet))
        pId = cursor.lastrowid

        self.connection.commit()
        cursor.close()
        return adID, userId, pId


    def update(self, first_name, last_name, email, password, role_id, address_id, phone_number, user_id):
        cursor = self.connection.cursor()
        updateQuery = ("update users "
        "set first_name = %s, last_name = %s, email = %s, password = %s, role_id = %s, address_id = %s, phone_number = %s "
        "where user_id = %s ")
        cursor.execute(updateQuery, (first_name, last_name, email, password, role_id, address_id, phone_number, user_id))
        pId = cursor.lastrowid
        self.connection.commit()
        cursor.close()


    def commit(self):
        self.connection.commit()


    def rollback(self):
        self.connection.rollback()