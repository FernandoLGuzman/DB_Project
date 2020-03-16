from flask import Blueprint
from flask import request

categories = Blueprint('categories', __name__)

@categories.route('/', methods = ['GET', 'POST'])
def category():
    if request.method == 'GET':
        #GET handle rcode
        return 'category GET'
    elif request.method == 'POST':
        #POST handler code
        return 'category POST'

@categories.route('/<int:id>', methods = ['GET', 'PUT', 'DELETE'])
def categoryById(id):
    if request.method == 'GET':
        #GET handler code
        return f'category/{id} GET'
    elif request.method == 'PUT':
        #PUT handler code
        return f'category/{id} PUT'
    elif request.method == 'DELETE':
        #DELETE handler code
        return f'category/{id} DELETE'
