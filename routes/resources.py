from flask import Blueprint
from flask import request

resources = Blueprint('resources', __name__)

@resources.route('/', methods = ['GET', 'POST'])
def resource_crud():
    if request.method == 'GET':
        #GET handler code
        return 'resource GET'
    elif request.method == 'POST':
        #POST handler code
        return 'resource POST'