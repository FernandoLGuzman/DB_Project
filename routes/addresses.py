from flask import Blueprint, request, jsonify
from handlers.addressHandler import AddressHandler

addresses = Blueprint('addresses', __name__)

@addresses.route('/', methods = ['GET', 'POST'])
def address():
    if request.method == 'GET':
        #GET handle rcode
        print(request.args)
        return AddressHandler().getAllAddresses(request.args)
    elif request.method == 'POST':
        #POST handler code
        print("REQUEST: ", request.json)
        return AddressHandler().insertAddress(request.json)

@addresses.route('/<int:id>', methods = ['GET', 'PUT', 'DELETE'])
def roleById(id):
    if request.method == 'GET':
        #GET handler code
        return AddressHandler().getAddressById(id)
    elif request.method == 'PUT':
        #PUT handler code
        return AddressHandler().updateAddress(id, request.json)
    elif request.method == 'DELETE':
        #DELETE handler code
        return AddressHandler().deleteAddress(id)
