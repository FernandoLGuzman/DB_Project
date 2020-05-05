from flask import jsonify
from dao.role import RoleDao

class RolesHandler:
    def __build_role_dict(self, row):
        result = {}
        result['role_id'] = row[0]
        result['role_name'] = row[1]
        return result


    def __build_role_attributes(self, role_id, name):
        result = {}
        result['role_id'] = role_id
        result['role_name'] = name
        return result


    def getRoles(self, args):
        userId = args.get('userId', None)
        roleName = args.get('roleName', None)
        limit = args.get('limit', 25)
        offset = args.get('offset', 0)
        orderBy = args.get('orderBy', 'rid')

        roleList = []
        if roleName and not userId:
            roleList = RoleDao.getRoleByName(roleName)
        elif not roleName and userId:
            roleList = RoleDao.getRoleByUser(userId)
        elif not roleName and not userId:
            roleList = RoleDao.getAllRoles(limit, offset, orderBy)
        else:
            return jsonify(Error = "Malformed get request"), 400

        result = []
        for row in roleList:
            result.append(self.__build_role_dict(row))

        return jsonify(Roles = result), 200

    def getRoleById(self, rid):
        role = RoleDao.getRoleById(rid)
        if not role:
            return jsonify(Error = "Role Not Found"), 404
        result = self.__build_role_dict(role)
        return jsonify(Role = result), 200


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
