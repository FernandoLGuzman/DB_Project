from flask import Blueprint, request, jsonify
from handlers.paymentMethodHandler import PaymentsMethodHandler

payments = Blueprint('payments', __name__)

@payments.route('/', methods = ['GET', 'POST'])
def payment():
    if request.method == 'GET':
        #GET handle rcode
        print(request.args)
        return PaymentsMethodHandler().getPaymentMethods(request.args)
    elif request.method == 'POST':
        #POST handler code
        print("REQUEST: ", request.json)
        return PaymentsMethodHandler().insertPaymentMethod(request.json)

@payments.route('/<int:id>', methods = ['GET', 'PUT', 'DELETE'])
def roleById(id):
    if request.method == 'GET':
        #GET handler code
        return PaymentsMethodHandler().getPaymentMethodById(id)
    elif request.method == 'PUT':
        #PUT handler code
        return PaymentsMethodHandler().updatePaymentMethod(id, request.json)
    elif request.method == 'DELETE':
        #DELETE handler code
        return PaymentsMethodHandler().deletePaymentMethod(id)
