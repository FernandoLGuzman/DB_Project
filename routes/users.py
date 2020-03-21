from flask import Blueprint
from flask import request
from handlers.users import handler

users = Blueprint('users', __name__)

@users.route('/', methods = ['GET'])
def user():
    #GET handler code
    return 'user GET'

@users.route('/<int:id>', methods = ['GET', 'PUT', 'DELETE'])
def userById(id):
    if request.method == 'GET':
        #GET handler code
        return f'user/{id} GET'
    elif request.method == 'PUT':
        #PUT handler code
        return f'user/{id} PUT'
    elif request.method == 'DELETE':
    #else:?
        #DELETE handler code
        return f'user/{id} DELETE'

@users.route('/log_in', methods = ['GET'])
def userLogin():
    #GET handler code
    return 'user/log_in GET'

@users.route('/sign_up/<int:role>', methods = ['POST'])
def userSignup(role):
    #POST handler code
    return f'user/sign_up/{role} POST'
