from flask import Blueprint, request
from handlers.purchaseHandler import PurchaseHandler

purchases = Blueprint('purchases', __name__)

# unsure if methods are correct in routes, just wanted filler, less hardcoding
# GETs should be good, though

@purchases.route('/', methods = ['GET', 'POST'])
def purchase():
    if request.method == 'GET':
        print(request.args)
        return PurchaseHandler().getPurchases(request.args)
    elif request.method == 'POST':
        return PurchaseHandler().insertPurchase(request.json)

@purchases.route('/<int:id>',methods = ['GET', 'PUT', 'DELETE'])
def purchaseById(id):
    if request.method == 'GET':
        return PurchaseHandler().getPurchaseById(id)
    elif request.method == 'PUT':
        return PurchaseHandler().updatePurchase(id, request.json)
    elif request.method == 'DELETE':
        return PurchaseHandler().deletePurchase(id)
