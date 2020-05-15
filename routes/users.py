from flask import Blueprint, request, json, jsonify
from handlers.userHandler import UserHandler

users = Blueprint('users', __name__)

@users.route('/', methods = ['GET', 'POST'])
def user():
    if request.method == 'GET':
        #GET handler code
        limit = request.args.get('limit')
        offset = request.args.get('offset')
        orderBy = request.args.get('orderBy')
        if len(request.args) == 0:
            return UserHandler().getAllUsers(request.args)
        elif len(request.args) == 1 and (limit or offset or orderBy):
            return UserHandler().getAllUsers(request.args)
        elif len(request.args) == 2 and ((limit and offset) or (limit and orderBy) or (offset and orderBy)):
            return UserHandler().getAllUsers(request.args)
        elif len(request.args) == 3 and (limit and offset and orderBy):
            return UserHandler().getAllUsers(request.args)
        else:
            return UserHandler().searchUsers(request.args)
    elif request.method == 'POST':
        #POST handler code
        return UserHandler().insertUser(request.json)

@users.route('/<int:id>', methods = ['GET', 'PUT', 'DELETE'])
def userById(id):
    if request.method == 'GET':
        #GET handler code
        return UserHandler().getUserByID(id)
    elif request.method == 'PUT':
        #PUT handler code
        return UserHandler().updateUser(id, request.json)
    elif request.method == 'DELETE':
    #else:?
        #DELETE handler code
        return UserHandler().deleteUser(id)

@users.route('/log_in', methods = ['GET'])
def userLogin():
    #GET handler code
    return UserHandler().loginUser(request.json)

@users.route('/sign_up', methods = ['POST'])
def userSignup():
    #POST handler code
    form = request.json
    return UserHandler().signUpUser(form['Address'],form['User'],form['Payment_Method'])
