from flask import Blueprint, request, json
from handlers.userHandler import UserHandler
from handlers.addressHandler import AddressHandler

users = Blueprint('users', __name__)

@users.route('/', methods = ['GET'])
def user():
    #GET handler code
    if len(request.args) == 0:
        return UserHandler().getAllUsers()
    else:
        return UserHandler().searchUsers(request.args)

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
    reponse = AddressHandler().insertAddress(form['Address'])
    if reponse[1] == 201:
        aid = json.loads(reponse[0].get_data(True))['Address']['address_id']
        return UserHandler().insertUser(aid, form['User'])
    else:
        return reponse
