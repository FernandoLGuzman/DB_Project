from flask import Blueprint
from flask import request
from handlers.resourceHandler import ResourceHandler

resources = Blueprint('resources', __name__)

@resources.route('/', methods = ['GET', 'POST'])
def resource():
    if request.method == 'GET':
        #GET handler code
        print(request.args)
        return ResourceHandler().getResources(request.args)
    elif request.method == 'POST':
        #POST handler code
        return ResourceHandler().insertResource(request.json)

@resources.route('/<int:id>', methods = ['GET', 'PUT', 'DELETE'])
def resourceById(id):
    if request.method == 'GET':
        #GET handler code
        return ResourceHandler().getResourceById(id)
    elif request.method == 'PUT':
        #PUT handler code
        return ResourceHandler().updateResource(id, request.json)
    elif request.method == 'DELETE':
        #DELETE handler code
        return ResourceHandler().deleteResource(id)

@resources.route('/request', methods = ['GET', 'POST'])
def resourceRequest():
    if request.method == 'GET':
        #GET handler code
        return ResourceHandler().getResourceRequests(request.args)
    elif request.method == 'POST':
        #POST handler code
        return ResourceHandler().insertResourceRequest(request.json)

@resources.route('/request/<int:id>', methods = ['GET', 'PUT'])
def resourceRequestById(id):
    if request.method == 'GET':
        #GET handler code
        return ResourceHandler().getResourceRequestById(id)
    elif request.method == 'PUT':
        #PUT handler code
        return ResourceHandler().updateResourceRequest(id, request.json)

@resources.route('/purchase', methods = ['GET', 'POST'])
def resourcePurchase():
    if request.method == 'GET':
        #GET handler code
        return ResourceHandler().getResourcePurchases(request.args)
    elif request.method == 'POST':
        #POST handler code
        return ResourceHandler().insertResourcePurchase(request.json)

@resources.route('/purchase/<int:id>', methods = ['GET'])
def resourcePurchaseById(id):
    if request.method == 'GET':
        #GET handler code
        return ResourceHandler().getResourcePurchaseById(id)

@resources.route('/statistics', methods = ['GET'])
def resourceStatistics():
    #Get handler code
    return 'resource/statistics GET'
