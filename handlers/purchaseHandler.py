from flask import jsonify
from dao.purchase import PurchaseDao

class PurchaseHandler:
    def buildPurchase(self, row):
        purchase = {
        'purchase_id': row[1],
        'user_id': row[2],
        'resource_id': row[0],
        'quantity': row[3],
        'purchase_price': float(row[4]),
        'date': row[5],
        # 'address_id': row[7],
        # 'category_id': row[8],
        # 'resource_name': row[9],
        # 'description': row[10],
        # 'price': float(row[11]),
        # 'stock': row[12]
        }
        return purchase

    def getPurchases(self, args):
        userId = args.get('userId', None)
        resourceId = args.get('resourceId', None)
        resourceName = args.get('resourceName', None)
        date = args.get('date', None)
        price = args.get('price', None)
        limit = args.get('limit', 25)
        offset = args.get('offset', 0)
        orderBy = args.get('orderBy', 'PID')

        purchaseList = []
        if userId and not resourceId and not resourceName and not date and not price:
            purchaseList = PurchaseDao().getPurchasesByUserID(userId, limit, offset, orderBy)
        elif not userId and resourceId and not resourceName and not date and not price:
            purchaseList = PurchaseDao().getPurchasesByResourceID(resourceId, limit, offset, orderBy)
        elif userId and resourceId and not resourceName and not date and not price:
            purchaseList = PurchaseDao().getPurchasesByUserIDAndResourceID(userId, resourceId, limit, offset, orderBy)
        elif not userId and not resourceId and resourceName and not date and not price:
            purchaseList = PurchaseDao().getPurchasesByResourceName(resourceName, limit, offset, orderBy)
        elif not userId and not resourceId and not resourceName and date and not price:
            purchaseList = PurchaseDao().getPurchasesByDate(date, limit, offset, orderBy)
        elif not userId and not resourceId and not resourceName and not date and price:
            purchaseList = PurchaseDao().getPurchasesByPrice(price, limit, offset, orderBy)
        elif not userId and not resourceId and not resourceName and not date and not price:
            purchaseList = PurchaseDao().getAllPurchases(limit, offset, orderBy)
        else:
            return jsonify(Error = "Malformed Get Request"), 400
        
        result = []
        for row in purchaseList:
            result.append(self.buildPurchase(row))
        
        return jsonify(Purchases = result), 200

    def getPurchaseById(self, pid):
        purchase = PurchaseDao().getPurchaseByID(pid)
        if not purchase:
            return jsonify(Error = "Purchase Not Found"), 404
        result = self.buildPurchase(purchase)
        return result
    
    def insertPurchase(self, json):
        # TODO later
        userId = json['user_id']
        resourceId = json['resource_id']
        quantity = json['quantity']
        price = json['purchase_price']
        if userId and resourceId and quantity:
            pid = PurchaseDao().insertPurchase(userId, resourceId, quantity, price)
            purchase = self.getPurchaseById(pid)
            result = self.buildPurchase(purchase) # returns error despite being pushed to DB
            return jsonify(PurchaseDao=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400


    def updatePurchase(self, pid, args):
        # TODO later
        return

    def deletePurchase(self, pid):
        # TODO later
        return
