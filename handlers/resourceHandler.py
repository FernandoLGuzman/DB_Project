from flask import jsonify
import datetime
from dao.resource import ResourceDao

class ResourceHandler:

    def buildResource(self, row):
        resource = {
            'resource_id': row[3],
            'user_id': row[4],
            'resource_name': row[5],
            'description': row[6],
            'price': float(row[7]),
            'stock': row[8],
            'category': {
                'category_id': row[2],
                'category_name': row[9],
                'parent_category': row[10]
            },
            'resource_location': {
                'address_id': row[1],
                'street_address': row[11],
                'city': row[12],
                'country': row[13],
                'zip_code': row[14],
                'latitud': float(row[15]),
                'longitud': float(row[16]),
                'senate_region':{
                    'region_id': row[0],
                    'name': row[17]
                }
            }
        }
        return resource

    def getResources(self, args):
        userId = args.get('userId', None)
        senateRegion = args.get('senateRegion', None)
        categoryId = args.get('categoryId', None)
        requested = args.get('requested', None)
        keywords = args.get('keywords', None)
        minStock = args.get('minStock', 0)
        minPrice = args.get('minPrice', 0)
        maxPrice = args.get('maxPrice', 9999999999999.99)
        limit = args.get('limit', 25)
        offset = args.get('offset', 0)
        orderBy = args.get('orderBy', 'name')

        resourceList = []

        if userId and categoryId and not requested and not senateRegion and not keywords:
            resourceList = ResourceDao().getResourcesByCategoryAndSupplier(categoryId, userId, minStock, minPrice, maxPrice, limit, offset, orderBy)

        elif categoryId and senateRegion and not userId and not requested and not keywords:
            resourceList = ResourceDao().getResourcesByCategoryAndSenateRegion(categoryId, senateRegion, minStock, minPrice, maxPrice, limit, offset, orderBy)

        elif requested and not categoryId and not userId and not senateRegion:
            if requested == 'true':
                if not keywords:
                    resourceList = ResourceDao().getAllRequestedResources(minStock, minPrice, maxPrice, limit, offset, orderBy)
                else:
                    resourceList = ResourceDao().getRequestedResourcesByKeywords(keywords, minStock, minPrice, maxPrice, limit, offset, orderBy)
            elif requested == 'false':
                if not keywords:
                    resourceList = ResourceDao().getAllUnrequestedResources(minStock, minPrice, maxPrice, limit, offset, orderBy)
                else:
                    resourceList = ResourceDao().getUnrequestedResourcesByKeywords(keywords, minStock, minPrice, maxPrice, limit, offset, orderBy)
            else:
                return jsonify(Error = "Malformed get request"), 400
        
        elif categoryId and not userId and not requested and not senateRegion and not keywords:
            resourceList = ResourceDao().getResourcesByCategory(categoryId, minStock, minPrice, maxPrice, limit, offset, orderBy)
        
        elif senateRegion and not categoryId and not requested and not userId and not keywords:
            resourceList = ResourceDao().getResourcesBySenateRegion(senateRegion, minStock, minPrice, maxPrice, limit, offset, orderBy)
        
        elif userId and not categoryId and not requested and not senateRegion and not keywords:
            resourceList = ResourceDao().getResourcesBySupplier(userId, minStock, minPrice, maxPrice, limit, offset, orderBy)
        
        elif keywords and not userId and not categoryId and not requested and not senateRegion:
            resourceList = ResourceDao().getResourcesByKeywords(keywords, minStock, minPrice, maxPrice, limit, offset, orderBy)

        elif not userId and not categoryId and not senateRegion and not requested and not keywords:
            resourceList = ResourceDao().getAllResources(minStock, minPrice, maxPrice, limit, offset, orderBy)
        
        else:
            return jsonify(Error = "Malformed get request"), 400

        result = []
        for row in resourceList:
            result.append(self.buildResource(row))

        return jsonify(Resources = result), 200

    def getResourceById(self, id):
        #dao logic
        resource = ResourceDao().getResourceById(id)
        if not resource:
            return jsonify(Error = "Resource Not Found"), 404
            
        result = self.buildResource(resource)

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
        if args == None or len(args) != 7:
            return jsonify(Error = 'Malformed post request'), 400
        try:
            uid = args['user_id']
            aid = args['address_id']
            cid = args['category_id']
            name = args['resource_name']
            description = args['description']
            price = args['price']
            stock = args['stock']
            if uid and aid and cid and name and description and price and stock:
                #dao logic
                resourceId = ResourceDao().insertResource(uid, aid, cid, name, description, price, stock)
                resource = ResourceDao().getResourceById(resourceId)
                result = self.buildResource(resource)
                return jsonify(Resource = result), 201
            else:
                return jsonify(Error = 'Attributes must not be null'), 400
        except:
            return jsonify(Error = 'Unexpected attributes in post request'), 400

    # def insertResourceRequest(self, args):
    #     if len(args) != 4:
    #         return jsonify(Error = 'Malformed post request'), 400

    #     try:
    #         uid = args['user_id']
    #         rid = args['resource_id']
    #         quantity = args['quantity']
    #         date = args['date']
    #         if uid and rid and quantity and date:
    #             #dao logic
    #             result = self.buildResourceRequest([0, uid, rid, quantity, date])
    #             return jsonify(ResourceRequest = result), 201
    #         else:
    #             return jsonify(Error = 'Attributes must not be null'), 400
    #     except:
    #         return jsonify(Error = 'Unexpected attributes in post request'), 400

    # def insertResourcePurchase(self, args):
    #     if len(args) != 4:
    #         return jsonify(Error = 'Malformed post request'), 400
    #     try:
    #         uid = args['user_id']
    #         rid = args['resource_id']
    #         quantity = args['quantity']
    #         date = args['date']
    #         if uid and rid and quantity and date:
    #             #dao logic
    #             result = self.buildResourceRequest([0, uid, rid, quantity, date])
    #             return jsonify(ResourceRequest = result), 201
    #         else:
    #             return jsonify(Error = 'Attributes must not be null'), 400
    #     except:
    #         return jsonify(Error = 'Unexpected attributes in post request'), 400

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

    # def updateResourceRequest(self, id, args):
    #     # if not in db:
    #     #     return jsonify(Error = 'Resource request not found'), 404
    #     if len(args) != 4:
    #         return jsonify(Error = 'Malformed post request'), 400

    #     try:
    #         uid = args['user_id']
    #         rid = args['resource_id']
    #         quantity = args['quantity']
    #         date = args['date']
    #         if uid and rid and quantity and date:
    #             #dao logic
    #             result = self.buildResourceRequest([id, uid, rid, quantity, date])
    #             return jsonify(ResourceRequest = result), 201
    #         else:
    #             return jsonify(Error = 'Attributes must not be null'), 400
    #     except:
    #         return jsonify(Error = 'Unexpected attributes in post request'), 400

    def restockResource(self, resourceId, args):
        #dao logic
        return jsonify(Restock = "Success"), 200

    def deleteResource(self, id):
        #dao logic
        return jsonify(Resource = {'id':id}), 200