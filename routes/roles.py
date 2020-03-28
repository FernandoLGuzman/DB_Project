from flask import Blueprint
from flask import request

roles = Blueprint('roles', __name__)

@roles.route('/', methods = ['GET', 'POST'])
def role():
    if request.method == 'GET':
        #GET handle rcode
        return 'category GET'
    elif request.method == 'POST':
        #POST handler code
        return 'category POST'

@roles.route('/<int:id>', methods = ['GET', 'PUT', 'DELETE'])
def roleById(id):
    if request.method == 'GET':
        #GET handler code
        return f'category/{id} GET'
    elif request.method == 'PUT':
        #PUT handler code
        return f'category/{id} PUT'
    elif request.method == 'DELETE':
        #DELETE handler code
        return f'category/{id} DELETE'
