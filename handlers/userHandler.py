from flask import jsonify
from dao.user import UserDao
# from dao.users import UsersDAO

class UserHandler:
    def __build_user_dict(self, row):
        result = {}
        result['user_id'] = row[3]
        result['first_name'] = row[4]
        result['last_name'] = row[5]
        result['email'] = row[6]
        result['password'] = row[7]
        result['phone_number'] = row[8]
        result['role'] = {
            'role_id': row[2],
            'role_name': row[9]
        }
        result['address'] = {
            'address_id': row[1],
            'street_address': row[10],
            'city': row[11],
            'coutry': row[12],
            'zip_code': row[13],
            'senate_region': {
                'region_id': row[0],
                'name': row[16]
            },
            'latitud': float(row[14]),
            'longitud': float(row[15])
        }
        return result


    def __build_user_attributes(self, uid, aid, rid, fname, lname, email, password, phone_number):
        result = {}
        result['user_id'] = uid
        result['address_id'] = aid
        result['role_id'] = rid
        result['first_name'] = fname
        result['last_name'] = lname
        result['email'] = email
        result['password'] = password
        result['phone_number'] = phone_number
        return result


    def getAllUsers(self):
        dao = UserDao()
        users_list = dao.getAllUsers()
        result_list = []
        for row in users_list:
            result = self.__build_user_dict(row)
            result_list.append(result)
        return jsonify(Users = result_list)


    def getUserByID(self, uid):
        dao = UserDao()
        row = dao.getUserById(uid)
        if not row: # hardcoded, delete later
            return jsonify(Error = "User Not Found"), 404
        else:
            user = self.__build_user_dict(row)
            return jsonify(User = user)


    def searchUsers(self, args): # can be redesigned based on implementation decisions
        fname = args.get("first_name")
        lname = args.get("last_name")
        email = args.get("email")
        phone_number = args.get("phone_number")
        # dao = UsersDAO()
        users_list = [[1, 2, 3, "name", "lname", "@yahoo", "123", "787"]] # hardcoded, empty later
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
        for row in users_list:
            result = self.__build_user_dict(row)
            result_list.append(result)
        return jsonify(Users = result_list)


    def getRolebyUserID(self, uid):
        # dao = UsersDAO()
        # if not dao.getUserByID(uid):
            # return jsonify(Error = "User not found."), 404
        # role = dao.getRolebyUserID(uid)
        role = [[uid, 2, 3, "name", "lname", "@yahoo", "123", "787"]] #hardcoded, delete later
        result = self.build_role_dict(role)
        return jsonify(Role = result)


    def loginUser(self, form):
        if len(form) != 2:
            return jsonify(Error = "Malformed login request."), 400
        else:
            try:
                email = form['email']
                password = form['password']
                if email and password:
                    dao = UserDao()
                    row = dao.loginUser(email,password)
                    if not row:
                        return jsonify(Error = "Incorrect email or password"), 400
                    else:
                        user = self.__build_user_dict(row)
                        return jsonify(User = user)
                else:
                    return jsonify(Error = "Attributes must not be null"), 400
            except:
                return jsonify(Error = 'Unexpected attributes in get request'), 400


    def insertUser(self, aid, form):
        if not form:
            return jsonify(Error = 'Empty Form'), 400
        print("form: ", form)
        if len(form) != 6:
            return jsonify(Error = "Malformed post request"), 400
        else:
            try:
                rid = form['role_id']
                fname = form['first_name']
                lname = form['last_name']
                email = form['email']
                password = form['password']
                phone_number = form['phone_number']
                if fname and lname and email and password and phone_number and rid:
                    # dao = UsersDAO()
                    uid = 0 # temp
                    # uid = dao.insert(fname, lname, email, password, phone_number)
                    result = self.__build_user_attributes(uid, aid, rid, fname, lname, email, password, phone_number)
                    return jsonify(User = result), 201
                else:
                    return jsonify(Error = "Attributes must not be null"), 400
            except:
                return jsonify(Error = 'Unexpected attributes in post request'), 400


    def deleteUser(self, uid):
        # dao = UsersDAO()
        # if not dao.getUserByID(uid):
        if False: # hardcoded, delete later
            return jsonify(Error = "User not found."), 404
        else:
            # dao.delete(uid)
            return jsonify(DeleteStatus = "OK"), 200


    def updateUser(self, uid, form):
        # dao = UsersDAO()
        # if not dao.getUserByID(uid):
        if False: # hardcoded, delete later
            return jsonify(Error = "User not found."), 404
        else:
            if len(form) != 7:
                return jsonify(Error = "Malformed update request."), 400
            else:
                try:
                    aid = form['address_id']
                    rid = form['role_id']
                    fname = form['first_name']
                    lname = form['last_name']
                    email = form['email']
                    password = form['password']
                    phone_number = form['phone_number']
                    if fname and lname and email and password and phone_number and aid and rid:
                        # dao = UsersDAO()
                        # dao.update(uid, aid, rid, fname, lname, email, password, phone_number)
                        result = self.__build_user_attributes(uid, aid, rid, fname, lname, email, password, phone_number)
                        return jsonify(User = result), 200
                    else:
                        return jsonify(Error = "Attributes must not be null"), 400
                except:
                    return jsonify(Error = 'Unexpected attributes in put request'), 400
