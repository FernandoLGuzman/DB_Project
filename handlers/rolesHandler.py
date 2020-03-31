from flask import jsonify
class RolesHandler:
    def __build_role_dict(self, row):
        result = {}
        result['role_id'] = row[0]
        result['name'] = row[1]
        return result


    def __build_role_attributes(self, role_id, name):
        result = {}
        result['role_id'] = role_id
        result['name'] = name
        return result


    def getAllRoles(self):
        #dao = PartsDAO()
        roles_list = [[0, 'role'], [1, 'role2']]
        #roles_list = dao.getAllParts()
        result_list = []
        for row in roles_list:
            result = self.__build_role_dict(row)
            result_list.append(result)
        return jsonify(Roles = result_list), 200


    def getRoleById(self, rid):
        roles_list = [[rid, 'role']]
        result_list = []
        for row in roles_list:
            result = self.__build_role_dict(row)
            result_list.append(result)
        return jsonify(Role = result_list), 200


    def insertRole(self, form):
        print("form: ", form)
        if len(form) != 1:
            return jsonify(Error = "Malformed post request"), 400
        else:
            try:
                name = form['name']
                if name:
                    #dao = PartsDAO()
                    rid = 0
                    #rid = dao.insert(name)
                    result = self.__build_role_attributes(rid, name)
                    return jsonify(Role=result), 201
                else:
                    return jsonify(Error="Attributes must not be null"), 400
            except:
                return jsonify(Error = 'Unexpected attributes in post request'), 400


    def updateRole(self, rid, form):
        # dao = PartsDAO()
        # if not dao.getPartById(rid):
        #     return jsonify(Error = "Part not found."), 404
        # else:
            if len(form) != 1:
                return jsonify(Error="Malformed update request"), 400
            else:
                try:
                    name = form['name']
                    if name:
                        # dao.update(rid, name)
                        result = self.__build_role_attributes(rid, name)
                        return jsonify(Role=result), 200
                    else:
                        return jsonify(Error="Attributes must not be null"), 400
                except:
                    return jsonify(Error = 'Unexpected attributes in put request'), 400


    def deleteRole(self, rid):
        #dao = PartsDAO()
        # if not dao.getPartById(rid):
        #     return jsonify(Error = "Part not found."), 404
        # else:
            # dao.delete(rid)
        return jsonify(DeleteStatus = "OK"), 200
