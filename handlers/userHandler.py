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
        return jsonify(Users = result_list)

    def getUserByID(self, uid):
        # dao = UsersDAO()
        # row = dao.getUserByID(uid)
        # if not row:
        if False: # hardcoded, duh
            return jsonify(Error = "Part Not Found"), 404
        else:
            # user = self.build_user_dict(row)
            user = []
            return jsonify(User = user)

    def searchUsers(self, args): # can be redesigned based on implementation decisions
        fname = args.get("first_name")
        lname = args.get("last_name")
        email = args.get("email")
        phone_number = args.get("phone_number")
        # dao = UsersDAO()
        users_list = []
        if (len(args) == 2) and fname and lname:
            # users_list = dao.getUsersByLastName(lname)
            print("Searching Users by First and Last Name") # hardcoded
        elif (len(args) == 1) and email:
            # users_list = dao.getUsersByEmail(email)
            print("Searching Users by Email") # hardcoded
        elif (len(args) == 1) and phone_number:
            # users_list = dao.getUsersByPhoneNumber(phone_number)
            print("Getting Users by Phone Number") # hardcoded
        else:
            return jsonify(Error = "Malformed query string"), 400
        result_list = []
        # for row in users_list:
            # result = self.build_user_dict(row)
            # result_list.append(result)
        return jsonify(Users = result_list)

    def getRolebyUserID(self, uid):
        # dao = UsersDAO()
        # if not dao.getUserByID(uid):
            # return jsonify(Error = "User not found."), 404
        # role = dao.getRolebyUserID(uid)
        # result = self.build_role_dict(role)
        result = []
        return jsonify(Role = result)

    def insertUser(self, form):
        print("form: ", form)
        if len(form) != 5:
            return jsonify(Error = "Malformed post request"), 400
        else:
            fname = form['first_name']
            lname = form['last_name']
            email = form['email']
            password = form['password']
            phone_number = form['phone_number']
            if fname and lname and email and password and phone_number:
                # dao = UsersDAO()
                # uid = dao.insert(fname, lname, email, password, phone_number)
                # result = self.build_user_attributes(uid, fname, lname, email, password, phone_number)
                result = []
                return jsonify(User=result), 201
            else:
                return jsonify(Error = 'Unexpected attributes in post request'), 400

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
            result = []
            return jsonify(User = result), 201
        else:
            return jsonify(Error = 'Unexpected attributes in post request'), 400

    def deleteUser(self, uid):
        # dao = UsersDAO()
        # if not dao.getUserByID(uid):
        if False: # hardcoded, duh
            return jsonify(Error = "User not found."), 404
        else:
            # dao.delete(uid)
            return jsonify(DeleteStatus = "OK"), 200 # tab when dao is finished, or not

    def updateUser(self, uid, form):
        # dao = UsersDAO()
        # if not dao.getUserByID(uid):
        if False: # hardcoded, duh
            return jsonify(Error = "User not found."), 404
        else:
            if len(form) != 5:
                return jsonify(Error = "Malformed update request."), 400
            else:
                fname = form['first_name']
                lname = form['last_name']
                email = form['email']
                password = form['password']
                phone_number = form['phone_number']
                if fname and lname and email and password and phone_number:
                    # dao = UsersDAO()
                    # dao.update(uid, fname, lname, email, password, phone_number)
                    # result = self.build_user_attributes(uid, fname, lname, email, password, phone_number)
                    result = []
                    return jsonify(User = result), 200
                else:
                    return jsonify(Error = 'Unexpected attributes in update request'), 400
