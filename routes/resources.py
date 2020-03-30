from flask import Blueprint
from flask import request
from handlers.resourceHandler import ResourceHandler

resources = Blueprint('resources', __name__)

@resources.route('/', methods = ['GET', 'POST'])
def resource():
    if request.method == 'GET':
        #GET handler code
        result = ResourceHandler().getAllResources(request.args)
        return 'resource GET'
    elif request.method == 'POST':
        #POST handler code
        result = ResourceHandler().insertResource(request.json)
        return 'resource POST'

@resources.route('/<int:id>', methods = ['GET', 'PUT', 'DELETE'])
def resourceById(id):
    if request.method == 'GET':
        #GET handler code
        result = ResourceHandler().getResourceById(id)
        return f'resource/{id} GET'
    elif request.method == 'PUT':
        #PUT handler code
        result = ResourceHandler().updateResource(id, request.json)
        return f'resource/{id} PUT'
    elif request.method == 'DELETE':
        #DELETE handler code
        result = ResourceHandler().deleteResource(id)
        return f'resource/{id} DELETE'

@resources.route('/request', methods = ['GET', 'POST'])
def resourceRequest():
    if request.method == 'GET':
        #GET handler code
        result = ResourceHandler().getResourceRequests(request.args)
        return 'resource/request GET'
    elif request.method == 'POST':
        #POST handler code
        result = ResourceHandler().insertResourceRequest(request.json)
        return 'resource/request POST'

@resources.route('/request/<int:id>', methods = ['GET', 'PUT'])
def resourceRequestById(id):
    if request.method == 'GET':
        #GET handler code
        result = ResourceHandler().getResourceRequestById(id)
        return f'resource/request/{id} GET'
    elif request.method == 'PUT':
        #PUT handler code
        result = ResourceHandler().updateResourceRequest(id, request.json)
        return f'resource/request/{id} PUT'

@resources.route('/purchase', methods = ['GET', 'POST'])
def resourcePurchase():
    if request.method == 'GET':
        #GET handler code
        result = ResourceHandler().getResourcePurchases(request.args)
        return 'resource/purchase GET'
    elif request.method == 'POST':
        #POST handler code
        result = ResourceHandler().insertResourcePurchase(request.json)
        return 'resource/purcahse POST'

@resources.route('/purchase/<int:id>', methods = ['GET'])
def resourcePurchaseById(id):
    if request.method == 'GET':
        #GET handler code
        result = ResourceHandler().getResourcePurchaseById(id)
        return f'resource/purchase/{id} GET'

@resources.route('/statistics', methods = ['GET'])
def resourceStatistics():
    #Get handler code
    return 'resource/statistics GET'
