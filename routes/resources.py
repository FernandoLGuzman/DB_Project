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

@resources.route('/<int:resourceId>/restock', methods = ['POST'])
def resourceRestock(resourceId):
    return ResourceHandler().restockResource(resourceId, request.json)

@resources.route('/statistics', methods = ['GET'])
def resourceStatistics():
    #Get handler code
    return 'resource/statistics GET'
