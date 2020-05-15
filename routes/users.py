from flask import Blueprint, request, json
from handlers.userHandler import UserHandler
from handlers.addressHandler import AddressHandler
from handlers.paymentMethodHandler import PaymentsMethodHandler

users = Blueprint('users', __name__)

@users.route('/', methods = ['GET'])
def user():
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
    # TODO add payment method
    #POST handler code
    form = request.json
    reponse = AddressHandler().insertAddress(form['Address'])
    if reponse[1] == 201:
        aid = json.loads(reponse[0].get_data(True))['Address']['address_id']
        return UserHandler().insertUser(aid, form['User'])
    else:
        return reponse
