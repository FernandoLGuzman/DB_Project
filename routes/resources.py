from flask import Blueprint
from flask import request

resources = Blueprint('resources', __name__)

@resources.route('/', methods = ['GET', 'POST'])
def resource():
    if request.method == 'GET':
        #GET handler code
        return 'resource GET'
    elif request.method == 'POST':
        #POST handler code
        return 'resource POST'

@resources.route('/<int:id>', methods = ['GET', 'PUT', 'DELETE'])
def resourceById(id):
    if request.method == 'GET':
        #GET handler code
        return f'resource/{id} GET'
    elif request.method == 'PUT':
        #PUT handler code
        return f'resource/{id} PUT'
    elif request.method == 'DELETE':
        #DELETE handler code
        return f'resource/{id} DELETE'

@resources.route('/request', methods = ['GET', 'POST'])
def resourceRequest():
    if request.method == 'GET':
        #GET handler code
        return 'resource/request GET'
    elif request.method == 'POST':
        #POST handler code
        return 'resource/request POST'

@resources.route('/request/<int:id>', methods = ['GET', 'PUT'])
def resourceRequestById(id):
    if request.method == 'GET':
        #GET handler code
        return f'resource/request/{id} GET'
    elif request.method == 'PUT':
        #PUT handler code
        return f'resource/request/{id} PUT'

@resources.route('/purchase', methods = ['GET', 'POST'])
def resourcePurchase():
    if request.method == 'GET':
        #GET handler code
        return 'resource/purchase GET'
    elif request.method == 'POST':
        #POST handler code
        return 'resource/purcahse POST'

@resources.route('/purchase/<int:id>', methods = ['GET', 'PUT'])
def resourcePurchaseById(id):
    if request.method == 'GET':
        #GET handler code
        return f'resource/purchase/{id} GET'
    elif request.method == 'PUT':
        #PUT handler code
        return f'resource/purcahse/{id} PUT'

@resources.route('/statistics', methods = ['GET'])
def resourceStatistics():
    #Get handler code
    return 'resource/statistics GET'
