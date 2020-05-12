from flask import jsonify
from dao.senate_regions import RegionsDao

class RegionsHandler:
    def __build_region_dict(self, row):
        result = {}
        result['region_id'] = row[0]
        result['name'] = row[1]
        return result


    def __build_region_attributes(self, region_id, name):
        result = {}
        result['region_id'] = region_id
        result['name'] = name
        return result


    def getRegions(self, args):
        name = args.get('name', None)
        limit = args.get('limit', 25)
        offset = args.get('offset', 0)
        orderBy = args.get('orderBy', 'rid')
        dao = RegionsDao()
        regionsList = []
        result = []
        if name:
            regionsList = dao.getRegionByName(name)
            result.append(self.__build_region_dict(regionsList))
        elif not name:
            regionsList = dao.getAllRegions(limit,offset,orderBy)
            for row in regionsList:
                result.append(self.__build_region_dict(row))
        else:
            return jsonify(Error = "Malformed get request"), 400

        return jsonify(Regions = result), 200


    def getRegionById(self, rid):
        dao = RegionsDao()
        region = dao.getRegionById(rid)
        if not region:
            return jsonify(Error = "Region Not Found"), 404
        result = self.__build_region_dict(region)
        return jsonify(Region = result), 200


    def insertRegion(self, form):
        print("form: ", form)
        if len(form) != 1:
            return jsonify(Error = "Malformed post request"), 400
        else:
            try:
                name = form['name']
                if name:
                    #dao = PartsDAO()
                    rid = 0
                    #rid = dao.insert(name)
                    result = self.__build_region_attributes(rid, name)
                    return jsonify(Region=result), 201
                else:
                    return jsonify(Error="Attributes must not be null"), 400
            except:
                return jsonify(Error = 'Unexpected attributes in post request'), 400


    def updateRegion(self, rid, form):
        # dao = PartsDAO()
        # if not dao.getPartById(rid):
        #     return jsonify(Error = "Part not found."), 404
        # else:
            if len(form) != 1:
                return jsonify(Error="Malformed update request"), 400
            else:
                try:
                    name = form['name']
                    if name:
                        # dao.update(rid, name)
                        result = self.__build_region_attributes(rid, name)
                        return jsonify(Region=result), 200
                    else:
                        return jsonify(Error="Attributes must not be null"), 400
                except:
                    return jsonify(Error = 'Unexpected attributes in put request'), 400


    def deleteRegion(self, rid):
        #dao = PartsDAO()
        # if not dao.getPartById(rid):
        #     return jsonify(Error = "Part not found."), 404
        # else:
            # dao.delete(rid)
        return jsonify(DeleteStatus = "OK"), 200
