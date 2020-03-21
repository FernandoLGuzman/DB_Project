from flask import jsonify
# from dao.users import UsersDAO

class UserHandler:
    def build_user_dict(self, row):
        result = {}
        result['user_id'] = row[0]
        result['first_name'] = row[1]
        result['last_name'] = row[2]
        result['email'] = row[3]
        result['password'] = row[4]
        result['phone_number'] = row[5] # have as foreign key to phone table?
        return result

    def build_user_attributes(self, uid, fname, lname, email, password, phone_number):
        result = {}
        result['uid'] = uid
        result['first_name'] = fname
        result['last_name'] = lname
        result['email'] = email
        result['password'] = password
        result['phone_number'] = phone_number
        return result

    def getAllUsers(self):
        # dao = UsersDAO()
        # users_list = dao.getAllUsers()
        result_list = []
        # for row in users_list:
            # result = self.build_user_dict(row)
            # result_list.append(result)
        # finish up, or hardcode
        return jsonify(Users=result_list)

    def getUserByID(self, uid):
        # dao = UsersDAO()
        # row = dao.getUserByID(uid)
        row = []
        if not row:
            return jsonify(Error = "Part Not Found"), 404
        else:
            user = []
            # user = self.build_user_dict(row)
            return jsonify(User = user)

    def searchUsers(self, args):
        # TODO
        return 0

    def getUsersbyRoleID(self, rid): # here or in role handler?
        # TODO
        return 0

    def insertUser(self, form):
        print("form: ", form)
        if len(form) != 5:
            return jsonify(Error = "Malformed post request"), 400
        else:
            fname = json['first_name']
            lname = json['last_name']
            email = json['email']
            password = json['password']
            phone_number = json['phone_number']
            if fname and lname and email and password and phone_number:
                # dao = UsersDAO()
                # uid = dao.insert(fname, lname, email, password, phone_number)
                # result = self.build_user_attributes(uid, fname, lname, email, password, phone_number)
                # return jsonify(User=result), 201
                return 0
            else:
                return jsonify(Error='Unexpected attributes in post request'), 400

    def insertUserJson(self, json):
        fname = json['first_name']
        lname = json['last_name']
        email = json['email']
        password = json['password']
        phone_number = json['phone_number']
        if fname and lname and email and password and phone_number:
            # dao = UsersDAO()
            # uid = dao.insert(fname, lname, email, password, phone_number)
            # result = self.build_user_attributes(uid, fname, lname, email, password, phone_number)
            # return jsonify(User=result), 201
            return 0
        else:
            return jsonify(Error='Unexpected attributes in post request'), 400

    def deleteUser(self, uid):
        # TODO
        return 0

    def updateUser(self, uid, form):
        # TODO
        return 0
