from flask import jsonify
import datetime
import dao.resource
from dao.resource import ResourceDao

class ResourceHandler:

    def buildResource(self, row):
        resource = {
            'resource_id': row[2],
            'user_id': row[3],
            'resource_name': row[4],
            'description': row[5],
            'price': row[6],
            'stock': row[7],
            'category': {
                'category_id': row[1],
                'category_name': row[8],
                'parent_category': row[9]
            },
            'resource_location': {
                'address_id': row[0],
                'street_address': row[10],
                'city': row[11],
                'country': row[12],
                'zip_code': row[13],
                'senate_region': row[14],
                'latitud': row[15],
                'longitud': row[16]
            }
        }
        #TODO add supplier name and category name for ui to  use 
        # resource['resource_id'] = row[0]
        # resource['supplier_id'] = row[1]
        # resource['address_id'] = row[2]
        # resource['category_id'] = row[3]
        # resource['name'] = row[4]
        # resource['description'] = row[5]
        # resource['price'] = row[6]
        # resource['stock'] = row[7]
        return resource

    def buildResourceRequest(self, row):
        request = {}
        request['request_id'] = row[0]
        request['user_id'] = row[1]
        request['resource_id'] = row[2]
        request['quantity'] = row[3]
        request['date'] = row[4]
        return request

    def buildResourcePurchase(self, row):
        purchase = {}
        purchase['purchase_id'] = row[0]
        purchase['user_id'] = row[1]
        purchase['resource_id'] = row[2]
        purchase['quantity'] = row[3]
        purchase['date'] = row[4]
        return purchase

    def getResources(self, args):
        userId = args.get('userId', None)
        senateRegion = args.get('senateRegion', None)
        categoryId = args.get('categoryId', None)
        minStock = args.get('minStock', 0)
        minPrice = args.get('minPrice', 0)
        maxPrice = args.get('maxPrice', 9999999999999.99)
        limit = args.get('limit', 25)
        offset = args.get('offser', 0)
        orderBy = args.get('orderBy', 'name')

        resourceList = []

        if userId and categoryId:
            resourceList = ResourceDao().getResourcesByCategoryAndSupplier(categoryId, userId, minStock, minPrice, maxPrice, limit, offset, orderBy)
        elif categoryId and senateRegion:
            resourceList = ResourceDao().getResourcesByCategoryAndSenateRegion(categoryId, senateRegion, minStock, minPrice, maxPrice, limit, offset, orderBy)
        elif categoryId:
            resourceList = ResourceDao().getResourcesByCategory(categoryId, minStock, minPrice, maxPrice, limit, offset, orderBy)
        elif senateRegion:
            resourceList = ResourceDao().getResourcesBySenateRegion(senateRegion, minStock, minPrice, maxPrice, limit, offset, orderBy)
        elif userId:
            resourceList = ResourceDao().getResourcesBySupplier(userId, minStock, minPrice, maxPrice, limit, offset, orderBy)
        else:
            resourceList = ResourceDao().getAllResources(minStock, minPrice, maxPrice, limit, offset, orderBy)

        result = []
        for row in resourceList:
            result.append(self.buildResource(row))

        #dao logic including filtering ordering and limiting
        # result = [self.buildResource([2312, 3452, 235, 5, 'Nike Shoe', 'Its a shoe, what did you expect?', 100, 20])]
        return jsonify(Resources = result), 200

    def getResourceById(self, id):
        #dao logic
        result = self.buildResource([id, 3452, 235, 5, 'Nike Shoe', 'Its a shoe, what did you expect?', 100, 20])
        return jsonify(Resource = result), 200

    def getResourceRequests(self, args):
        limit = args.get('limit', 50)
        orderBy = args.get('orderBy', None)
        #dao logic including filtering ordering and limiting
        result = [self.buildResourceRequest([3, 34, 26224, 10, datetime.datetime.now()])]
        return jsonify(ResourceRequests = result), 200

    def getResourceRequestById(self, id):
        #dao logic
        result = self.buildResourceRequest([id, 34, 26224, 10, datetime.datetime.now()])
        return jsonify(ResourceRequest = result), 200

    def getResourcePurchases(self, args):
        limit = args.get('limit', 50)
        orderBy = args.get('orderBy', None)
        #dao logic including filtering ordering and limiting
        result = [self.buildResourcePurchase([3, 34, 26224, 10, datetime.datetime.now()])]
        return jsonify(ResourcePurchases = result), 200

    def getResourcePurchaseById(self, id):
        #dao logic
        result = self.buildResourcePurchase([id, 34, 26224, 10, datetime.datetime.now()])
        return jsonify(ResourcePurchase = result), 200

    def insertResource(self, args):
        if len(args) != 7:
            return jsonify(Error = 'Malformed post request'), 400
        try:
            sid = args['supplier_id']
            aid = args['address_id']
            cid = args['category_id']
            name = args['name']
            description = args['description']
            price = args['price']
            stock = args['stock']
            if sid and aid and cid and name and description and price and stock:
                #dao logic
                result = self.buildResource([0, sid, aid, cid, name, description, 100, 20])
                return jsonify(Resource = result), 201
            else:
                return jsonify(Error = 'Attributes must not be null'), 400
        except:
            return jsonify(Error = 'Unexpected attributes in post request'), 400

    def insertResourceRequest(self, args):
        if len(args) != 4:
            return jsonify(Error = 'Malformed post request'), 400

        try:
            uid = args['user_id']
            rid = args['resource_id']
            quantity = args['quantity']
            date = args['date']
            if uid and rid and quantity and date:
                #dao logic
                result = self.buildResourceRequest([0, uid, rid, quantity, date])
                return jsonify(ResourceRequest = result), 201
            else:
                return jsonify(Error = 'Attributes must not be null'), 400
        except:
            return jsonify(Error = 'Unexpected attributes in post request'), 400

    def insertResourcePurchase(self, args):
        if len(args) != 4:
            return jsonify(Error = 'Malformed post request'), 400
        try:
            uid = args['user_id']
            rid = args['resource_id']
            quantity = args['quantity']
            date = args['date']
            if uid and rid and quantity and date:
                #dao logic
                result = self.buildResourceRequest([0, uid, rid, quantity, date])
                return jsonify(ResourceRequest = result), 201
            else:
                return jsonify(Error = 'Attributes must not be null'), 400
        except:
            return jsonify(Error = 'Unexpected attributes in post request'), 400

    def updateResource(self, id, args):
        # if id not in db:
        #     return jsonify(Error = 'Resource not found'), 404
        if len(args) != 7:
            return jsonify(Error = 'Malformed post request'), 400
        
        try:
            sid = args['supplier_id']
            aid = args['address_id']
            cid = args['category_id']
            name = args['name']
            description = args['description']
            price = args['price']
            stock = args['stock']
            if sid and aid and cid and name and description and price and stock:
                #dao logic
                result = self.buildResource([id, sid, aid, cid, name, description, 100, 20])
                return jsonify(Resource = result), 201
            else:
                return jsonify(Error = 'Attributes must not be null'), 400
        except:
            return jsonify(Error = 'Unexpected attributes in post request'), 400

    def updateResourceRequest(self, id, args):
        # if not in db:
        #     return jsonify(Error = 'Resource request not found'), 404
        if len(args) != 4:
            return jsonify(Error = 'Malformed post request'), 400

        try:
            uid = args['user_id']
            rid = args['resource_id']
            quantity = args['quantity']
            date = args['date']
            if uid and rid and quantity and date:
                #dao logic
                result = self.buildResourceRequest([id, uid, rid, quantity, date])
                return jsonify(ResourceRequest = result), 201
            else:
                return jsonify(Error = 'Attributes must not be null'), 400
        except:
            return jsonify(Error = 'Unexpected attributes in post request'), 400

    def restockResource(self, resourceId, args):
        #dao logic
        return jsonify(Restock = "Success"), 200

    def deleteResource(self, id):
        #dao logic
        return jsonify(Resource = {'id':id}), 200