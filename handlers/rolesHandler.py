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


    def getRoleById(self, pid):
        roles_list = [[pid, 'role']]
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
            name = form['name']
            if name:
                #dao = PartsDAO()
                pid = 0
                #pid = dao.insert(name)
                result = self.__build_role_attributes(pid, name)
                return jsonify(Part=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400


    def updateRole(self, pid, form):
        # dao = PartsDAO()
        # if not dao.getPartById(pid):
        #     return jsonify(Error = "Part not found."), 404
        # else:
            if len(form) != 1:
                return jsonify(Error="Malformed update request"), 400
            else:
                name = form['name']
                if name:
                    # dao.update(pid, name)
                    result = self.__build_role_attributes(pid, name)
                    return jsonify(Part=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400


    def deleteRole(self, pid):
        #dao = PartsDAO()
        # if not dao.getPartById(pid):
        #     return jsonify(Error = "Part not found."), 404
        # else:
            # dao.delete(pid)
        return jsonify(DeleteStatus = "OK"), 200
