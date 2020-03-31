from flask import Blueprint, request, jsonify
from handlers.rolesHandler import RolesHandler

roles = Blueprint('roles', __name__)

@roles.route('/', methods = ['GET', 'POST'])
def role():
    if request.method == 'GET':
        #GET handle rcode
        return RolesHandler().getAllRoles()
    elif request.method == 'POST':
        #POST handler code
        print("REQUEST: ", request.json)
        return RolesHandler().insertRole(request.json)

@roles.route('/<int:id>', methods = ['GET', 'PUT', 'DELETE'])
def roleById(id):
    if request.method == 'GET':
        #GET handler code
        return RolesHandler().getRoleById(id)
    elif request.method == 'PUT':
        #PUT handler code
        return RolesHandler().updateRole(id, request.json)
    elif request.method == 'DELETE':
        #DELETE handler code
        return RolesHandler().deleteRole(id)
