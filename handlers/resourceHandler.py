from flask import jsonify
class ResourceHandler:

    def getAllResources(self, args):
        limit = args.get('limit')
        orderBy = args.get('orderBy')
        return jsonify(Resources = 'Coming soon'), 200

    def getResourceById(self, id):

        return jsonify(Resource = {'id':id}), 200

    def getResourceRequests(self, args):

        return jsonify(ResourceRequests = 'Coming soon'), 200

    def getResourceRequestById(self, id):

        return jsonify(ResourceRequest = {'id':id}), 200

    def getResourcePurchases(self, args):

        return jsonify(ResourcePurchases = 'Coming soon'), 200

    def getResourcePurchaseById(self, id):

        return jsonify(ResourcePurchase = {'id':id}), 200

    def insertResource(self, args):

        return jsonify(Resource = 'Insert Coming soon'), 200

    def insertResourceRequest(self, args):

        return jsonify(ResourceRequest = 'Insert Coming soon'), 200

    def insertResourcePurchase(self, args):

        return jsonify(ResourcePurchase = 'Insert Coming soon'), 200

    def updateResource(self, id, args):

        return jsonify(Resource = {'id':id}, Status = 'Update Comming Soon'), 200

    def updateResourceRequest(self, id, args):

        return jsonify(ResourceRequest = {'id':id}, Status = 'Update Comming Soon'), 200

    def deleteResource(self, id):

        return jsonify(Resource = {'id':id}), 200