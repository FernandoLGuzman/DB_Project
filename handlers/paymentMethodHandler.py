from flask import jsonify
from dao.payment import PaymentDao

class PaymentsMethodHandler:
    def __build_payment_dict(self, row):
        result = {}
        result['payment_method_id'] = row[0]
        result['user_id'] = row[1]
        result['type'] = row[2]
        result['wallet'] = row[3]
        return result


    def __build_payment_attributes(self, pmID, user_id, type, wallet):
        result = {}
        result['payment_method_id'] = pmID
        result['user_id'] = user_id
        result['type'] = type
        result['wallet'] = wallet
        return result


    def getPaymentMethods(self, args):
        userId = args.get('userId', None)
        limit = args.get('limit', 25)
        offset = args.get('offset', 0)
        orderBy = args.get('orderBy', 'rid')
        dao = PaymentDao()
        paymList = []
        result = []
        if userId:
            paymList = dao.getPaymentMethodsByUserId(userId)
            result.append(self.__build_payment_dict(paymList))
        elif not userId:
            paymList = dao.getAllPaymentMethods(limit,offset,orderBy)
            for row in paymList:
                result.append(self.__build_payment_dict(row))
        else:
            return jsonify(Error = "Malformed get request"), 400

        return jsonify(PaymentsMethod = result), 200

    def getPaymentMethodById(self, pmid):
        dao = PaymentDao()
        pm = dao.getPaymentMethodById(pmid)
        if not pm:
            return jsonify(Error = "Payment Method Not Found"), 404
        result = self.__build_payment_dict(pm)
        return jsonify(PaymentsMethod = result), 200


    def insertPaymentMethod(self, form):
        print("form: ", form)
        if len(form) != 3:
            return jsonify(Error = "Malformed post request"), 400
        else:
            try:
                user_id = form['user_id']
                type = form['type']
                wallet = form['wallet']
                if user_id and type and wallet:
                    dao = PaymentDao()
                    pmid = dao.insert(user_id,type,wallet)
                    result = self.__build_payment_attributes(pmid,user_id,type,wallet)
                    return jsonify(PaymentsMethod=result), 201
                else:
                    return jsonify(Error="Attributes must not be null"), 400
            except:
                return jsonify(Error = 'Unexpected attributes in post request'), 400


    def updatePaymentMethod(self, pmid, form):
        # dao = PartsDAO()
        # if not dao.getPartById(rid):
        #     return jsonify(Error = "Part not found."), 404
        # else:
            if len(form) != 3:
                return jsonify(Error="Malformed update request"), 400
            else:
                try:
                    user_id = form['user_id']
                    type = form['type']
                    wallet = form['wallet']
                    if user_id and type and wallet:
                        # dao.update(rid, name)
                        result = self.__build_payment_attributes(pmid,user_id,type,wallet)
                        return jsonify(PaymentMethod=result), 200
                    else:
                        return jsonify(Error="Attributes must not be null"), 400
                except:
                    return jsonify(Error = 'Unexpected attributes in put request'), 400


    def deletePaymentMethod(self, rid):
        #dao = PartsDAO()
        # if not dao.getPartById(rid):
        #     return jsonify(Error = "Part not found."), 404
        # else:
            # dao.delete(rid)
        return jsonify(DeleteStatus = "OK"), 200
