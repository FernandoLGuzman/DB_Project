from flask import jsonify
class ResourceHandler:

    def getAllResources(args):
        limit = args.get('limit')
        orderBy = args.get('orderBy')
        return jsonify(Resources = 'Coming soon'), 200

    def getResourceById(id):

        return jsonify(Resource = 'Coming soon'), 200

    def getResourceRequests(args):

        return jsonify(ResourceRequests = 'Coming soon'), 200

    def getResourceRequestById(id):

        return jsonify(ResourceRequest = 'Coming soon'), 200

    def getResourcePurchases(args):

        return jsonify(ResourcePurchases = 'Coming soon'), 200

    def getResourcePurchaseById(id):

        return jsonify(ResourcePurchase = 'Coming soon'), 200

    def insertResource(args):

        return jsonify(Resource = 'Coming soon'), 200

    def insertResourceRequest(args):

        return jsonify(ResourceRequest = 'Coming soon'), 200

    def insertResourcePurchase(args):

        return jsonify(ResourcePurchase = 'Coming soon'), 200

    def updateResource(id, args):

        return jsonify(Resource = 'Coming soon'), 200

    def updateResourceRequest(id, args):

        return jsonify(ResourceRequest = 'Coming soon'), 200

    def deleteResource(id):

        return jsonify(Resource = 'Coming soon'), 200