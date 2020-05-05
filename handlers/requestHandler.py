from flask import jsonify
from dao.request import RequestDao

class RequestHandler:
    def buildRequest(self, row):
        request = {}
        request['request_id'] = row[0]
        request['user_id'] = row[1]
        request['resource_id'] = row[2]
        request['quantity'] = row[3]
        request['date'] = row[4]
        request['is_satisfied'] = row[5]

    def getRequests(self, args):
        userId = args.get('userId', None)
        resourceId = args.get('resourceId', None)
        resourceName = args.get('resourceName', None)
        date = args.get('date', None)
        isSatisfied = args.get('isSatisfied', None)
        limit = args.get('limit', 25)
        offset = args.get('offset',0)
        orderBy = args.get('orderBy', 'ReqID')

        requestList = []
        if userId and not resourceId and not resourceName and not date and not isSatisfied:
            requestList = RequestDao.getRequestsByUserID(userId, limit, offset, orderBy)
        elif not userId and resourceId and not resourceName and not date and not isSatisfied:
            requestList = RequestDao.getRequestsByResourceID(resourceId, limit, offset, orderBy)
        elif userId and resourceId and not resourceName and not date and not isSatisfied:
            requestList = RequestDao.getRequestsByUserIDAndResourceID(userId, resourceId, limit, offset, orderBy)
        elif not userId and not resourceId and resourceName and not date and not isSatisfied:
            requestList = RequestDao.getRequestsByResourceName(resourceName, limit, offset, orderBy)
        elif not userId and not resourceId and not resourceName and date and not isSatisfied:
            requestList = RequestDao.getRequestsByDate(date, limit, offset, orderBy)
        elif not userId and not resourceId and not resourceName and not date and isSatisfied:
            if isSatisfied == 0:
                requestList = RequestDao.getAllUnsatisfiedRequests(limit, offset, orderBy)
            elif isSatisfied == 1:
                requestList = RequestDao.getAllSatisfiedRequests(limit, offset, orderBy)
            else:
                return jsonify(Error = "Wrong isSatisfied parameter"), 400 # may not be correct code or way to do this
        elif not userId and not resourceId and not resourceName and not date and not isSatisfied:
            requestList = RequestDao.getAllRequests(limit, offset, orderBy)
        else:
            return jsonify(Error = "Malformed get request"), 400
        
        result = []
        for row in requestList:
            result.append(self.buildRequest(row))
        
        return jsonify(Requests = result), 200

    def getRequestById(self, reqid):
        request = RequestDao.getRequestByID(reqid)
        if not request:
            return jsonify(Error = "Request Not Found"), 404
        result = self.buildRequest(request)
        return result
    
    def insertRequest(self, args):
        # TODO later
        return

    def updateRequest(self, reqid, args):
        # TODO later
        return

    def deleteRequest(self, reqid):
        # TODO later
        return
