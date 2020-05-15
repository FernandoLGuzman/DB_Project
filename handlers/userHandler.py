from flask import jsonify
from handlers.addressHandler import AddressHandler
from handlers.paymentMethodHandler import PaymentsMethodHandler
from dao.user import UserDao
from dao.payment import PaymentDao

class UserHandler:
    def __build_user_dict(self, row):
        result = {}
        userID = row[3]
        result['user_id'] = userID
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
        dao = PaymentDao()
        plist = dao.getPaymentMethodsByUserId(userID)
        if plist:
            arr = []
            for line in plist:
                method =  {
                    'payment_method_id': line[0],
                    'type': line[2],
                    'wallet': float(line[3])
                }
                arr.append(method)
            result['payment_methods'] = arr
        else:
            result['payment_methods'] = None
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


    def getAllUsers(self, args):
        limit = args.get('limit', 25)
        offset = args.get('offset', 0)
        orderBy = args.get('orderBy', 'uid')
        limit = int(limit)
        offset = int(offset)
        dao = UserDao()
        users_list = dao.getAllUsers(limit,offset,orderBy)
        result_list = []
        for row in users_list:
            result = self.__build_user_dict(row)
            result_list.append(result)
        return jsonify(Users = result_list)


    def getUserByID(self, uid):
        dao = UserDao()
        row = dao.getUserById(uid)
        if not row:
            return jsonify(Error = "User Not Found"), 404
        else:
            user = self.__build_user_dict(row)
            return jsonify(User = user)


    def searchUsers(self, args): # can be redesigned based on implementation decisions
        fname = args.get("first_name")
        lname = args.get("last_name")
        email = args.get("email")
        phone_number = args.get("phone_number")
        role_name = args.get("role_name")
        rid = args.get("role_id")
        extra = 0
        if args.get('limit'):
            extra = extra + 1
        if args.get('offset'):
            extra = extra + 1
        if args.get('orderBy'):
            extra = extra + 1
        limit = args.get('limit', 25)
        offset = args.get('offset', 0)
        orderBy = args.get('orderBy', 'uid')
        limit = int(limit)
        offset = int(offset)
        dao = UserDao()
        users_list = []
        if (len(args) == 2 + extra) and fname and lname:
            users_list = dao.getUsersByFullName(fname=fname, lname=lname,limit=limit,offset=offset,orderBy=orderBy)
        elif (len(args) == 1 + extra) and email:
            users_list = dao.getUsersByEmail(email,limit,offset,orderBy)
        elif (len(args) == 1 + extra) and phone_number:
            users_list = dao.getUsersByPhoneNumber(phone_number,limit,offset,orderBy)
        elif (len(args) == 1 + extra) and (role_name or rid):
            if role_name:
                users_list = dao.getUsersByRoleName(roleName = role_name,limit=limit,offset=offset,orderBy=orderBy)
            else:
                users_list = dao.getUsersByRoleID(roleID=rid,limit=limit,offset=offset,orderBy=orderBy)
        else:
            return jsonify(Error = "Malformed query string"), 400
        result_list = []
        for row in users_list:
            result = self.__build_user_dict(row)
            result_list.append(result)
        return jsonify(Users = result_list)


    # def getRolebyUserID(self, uid):
    #     # dao = UsersDAO()
    #     # if not dao.getUserByID(uid):
    #         # return jsonify(Error = "User not found."), 404
    #     # role = dao.getRolebyUserID(uid)
    #     role = [[uid, 2, 3, "name", "lname", "@yahoo", "123", "787"]] #hardcoded, delete later
    #     result = self.build_role_dict(role)
    #     return jsonify(Role = result)


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


    def insertUser(self, form):
        if not form:
            return jsonify(Error = 'Empty Form'), 400
        print("form: ", form)
        if len(form) != 7:
            return jsonify(Error = "Malformed post request"), 400
        else:
            try:
                rid = form['role_id']
                fname = form['first_name']
                lname = form['last_name']
                email = form['email']
                password = form['password']
                phone_number = form['phone_number']
                address_id = form['address_id']
                if fname and lname and email and password and phone_number and rid and address_id:
                    dao = UserDao()
                    uid = dao.insert(fname,lname,email,password,rid,address_id,phone_number)
                    result = self.__build_user_attributes(uid, address_id, rid, fname, lname, email, password, phone_number)
                    return jsonify(User = result), 201
                else:
                    return jsonify(Error = "Attributes must not be null"), 400
            except Exception as e:
                return jsonify(Error = f'Unexpected attributes in post request; {e}'), 400


    def signUpUser(self, address, user, payment):
        if not address and not user:
            return jsonify(Error = 'Empty Address and User'), 400
        elif len(user) != 6:
            return jsonify(Error = "Malformed user post request"), 400
        elif len(address) != 7:
            return jsonify(Error = "Malformed address post request"), 400
        elif payment and len(payment) != 2:
            return jsonify(Error = "Malformed payment_method post request"), 400
        else:
            try:
                rid = user['role_id']
                fname = user['first_name']
                lname = user['last_name']
                email = user['email']
                password = user['password']
                phone_number = user['phone_number']

                street_address = address['street_address']
                city = address['city']
                country = address['country']
                zip_code = address['zip_code']
                senate_region = address['senate_region']
                latitud = address['latitud']
                longitud = address['longitud']
                if fname and lname and email and password and phone_number and rid and street_address and city and country and zip_code and senate_region and latitud and longitud:
                    if payment:
                        type = payment['type']
                        wallet = payment['wallet']
                        if type and wallet:
                            dao = UserDao()
                            aid, uid, pid = dao.signupWiPayment(fname,lname,email,password,rid,phone_number,street_address,city,country,zip_code,senate_region,latitud,longitud,type,wallet)
                            userres = self.__build_user_attributes(uid, aid, rid, fname, lname, email, password, phone_number)
                            addressres = AddressHandler().build_address_attributes(aid, street_address,city,country,zip_code,senate_region,latitud,longitud)
                            paymentres = PaymentsMethodHandler().build_payment_attributes(pid,uid,type,wallet)
                            return jsonify(User = userres, Address = addressres, Payment_Method = paymentres), 201
                        else:
                            return jsonify(Error = "Attributes must not be null"), 400
                    else:
                        dao = UserDao()
                        aid, uid = dao.signupNoPayment(fname,lname,email,password,rid,phone_number,street_address,city,country,zip_code,senate_region,latitud,longitud)
                        userres = self.__build_user_attributes(uid, aid, rid, fname, lname, email, password, phone_number)
                        addressres = AddressHandler().build_address_attributes(aid,street_address,city,country,zip_code,senate_region,latitud,longitud)
                        return jsonify(User = userres, Address = addressres), 201
                else:
                    return jsonify(Error = "Attributes must not be null"), 400
            except Exception as e:
                return jsonify(Error = f'Unexpected attributes in post request; {e}'), 400


    def deleteUser(self, uid):
        # dao = UsersDAO()
        # if not dao.getUserByID(uid):
        if False: # hardcoded, delete later
            return jsonify(Error = "User not found."), 404
        else:
            # dao.delete(uid)
            return jsonify(DeleteStatus = "OK"), 200


    def updateUser(self, uid, form):
        dao = UserDao()
        if not dao.getUserById(uid): # hardcoded, delete later
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
                        dao.update(fname,lname,email,password,rid,aid,phone_number,uid)
                        result = self.__build_user_attributes(uid, aid, rid, fname, lname, email, password, phone_number)
                        return jsonify(User = result), 200
                    else:
                        return jsonify(Error = "Attributes must not be null"), 400
                except Exception as e:
                    return jsonify(Error = f'Unexpected attributes in put request; {e}'), 400
