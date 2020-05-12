from flask import Blueprint, request, jsonify
from handlers.regionsHandler import RegionsHandler

regions = Blueprint('regions', __name__)

@regions.route('/', methods = ['GET', 'POST'])
def region():
    if request.method == 'GET':
        #GET handle rcode
        print(request.args)
        return RegionsHandler().getRegions(request.args)
    elif request.method == 'POST':
        #POST handler code
        print("REQUEST: ", request.json)
        return RegionsHandler().insertRegion(request.json)

@regions.route('/<int:id>', methods = ['GET', 'PUT', 'DELETE'])
def regionById(id):
    if request.method == 'GET':
        #GET handler code
        return RegionsHandler().getRegionById(id)
    elif request.method == 'PUT':
        #PUT handler code
        return RegionsHandler().updateRegion(id, request.json)
    elif request.method == 'DELETE':
        #DELETE handler code
        return RegionsHandler().deleteRegion(id)
