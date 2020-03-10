from flask import Blueprint
from flask import request

resources = Blueprint('resources', __name__)

@resources.route('/', methods = ['GET', 'POST'])
def resourceCRUD():
    if request.method == 'GET':
        #GET handler code
        return 'resource GET'
    elif request.method == 'POST':
        #POST handler code
        return 'resource POST'

@resources.route('/<int:id>', methods = ['GET', 'PUT', 'DELETE'])
def resourceCRUD(id):
    if request.method == 'GET':
        #GET handler code
        return 'resource/<id> GET'
    elif request.method == 'PUT':
        #PUT handler code
        return 'resource/<id> PUT'
    elif request.method == 'DELETE':
        #DELETE handler code
        return 'resource/<id> DELETE'

@resources.route('/request', methods = ['GET', 'POST'])
def requestCRUD():
    if request.method == 'GET':
        #GET handler code
        return 'resource/request GET'
    elif request.method == 'POST':
        #POST handler code
        return 'resource/request POST'

@resources.route('/request/<int:id>', methods = ['GET', 'PUT'])
def requestCRUD(id):
    if request.method == 'GET':
        #GET handler code
        return 'resource/request/<id> GET'
    elif request.method == 'PUT':
        #PUT handler code
        return 'resource/request/<id> PUT'

@resources.route('/purchase', method = ['GET', 'POST'])
def purchaseCRUD():
    if request.method == 'GET':
        #GET handler code
        return 'resource/purchase GET'
    elif request.method == 'POST':
        #POST handler code
        return 'resource/purcahse POST'

@resources.route('/purchase/<int:id>', method = ['GET', 'PUT'])
def purchaseCRUD(id):
    if request.method == 'GET':
        #GET handler code
        return 'resource/purchase/<id> GET'
    elif request.method == 'PUT':
        #PUT handler code
        return 'resource/purcahse/<id> PUT'

@resources.route('/statistics', methods = ['GET'])
def resourceStatistics():
    #Get handler code
    return 'resource/statistics GET'
