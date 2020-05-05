from flask import Blueprint, request
from handlers.requestHandler import RequestHandler

requests = Blueprint('requests', __name__)

# unsure if methods are correct in routes, just wanted filler, less hardcoding
# GETs should be good, though

@requests.route('/', methods = ['GET', 'POST'])
def requestR(): # request() already taken
    if request.method == 'GET':
        print(request.args)
        return RequestHandler().getRequests(request.args)
    elif request.method == 'POST':
        return RequestHandler().insertRequest(request.json)

@requests.route('/<int:id>',methods = ['GET', 'PUT', 'DELETE'])
def requestById(id):
    if request.method == 'GET':
        return RequestHandler().getRequestById(id)
    elif request.method == 'PUT':
        return RequestHandler().updateRequest(id, request.json)
    elif request.method == 'DELETE':
        return RequestHandler().deleteRequest(id)
