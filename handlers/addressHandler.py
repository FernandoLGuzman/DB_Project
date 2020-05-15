from flask import jsonify
from dao.address import AddressDao

class AddressHandler:
    def __build_address_dict(self, row):
        result = {}
        result['address_id'] = row[0]
        result['street_address'] = row[1]
        result['city'] = row[2]
        result['country'] = row[3]
        result['zip_code'] = row[4]
        result['senate_region'] = row[5]
        result['latitud'] = float(row[6])
        result['longitud'] = float(row[7])
        return result


    def __build_address_attributes(self, aid, street_address, city, country, zip_code, senate_region, latitud, longitud):
        result = {}
        result['address_id'] = aid
        result['street_address'] = street_address
        result['city'] = city
        result['country'] = country
        result['zip_code'] = zip_code
        result['senate_region'] = senate_region
        result['latitud'] = latitud
        result['longitud'] = longitud
        return result


    def getAllAddresses(self, args):
        dao = AddressDao()
        address_list = dao.getAllAddresses()
        result_list = []
        for row in address_list:
            result = self.__build_address_dict(row)
            result_list.append(result)
        return jsonify(Addresses = result_list), 200


    def getAddressById(self, aid):
        dao = AddressDao()
        address = dao.getAddressById(aid)
        if address:
            result_list = []
            result = self.__build_address_dict(address)
            result_list.append(result)
            return jsonify(Address = result_list), 200
        else:
            return jsonify(Error = "Address not Found"), 404


    def insertAddress(self, form):
        if not form:
            return jsonify(Error = "empty form"), 400
        print("form: ", form)
        if len(form) != 7:
            return jsonify(Error = "Malformed post request"), 400
        else:
            try:
                street_address = form['street_address']
                city = form['city']
                country = form['country']
                zip_code = form['zip_code']
                senate_region = form['senate_region']
                latitud = form['latitud']
                longitud = form['longitud']
                if street_address and city and country and zip_code and senate_region and latitud and longitud:
                    dao = AddressDao()
                    aid = dao.insert(street_address,city,country,zip_code, senate_region,latitud,longitud)
                    result = self.__build_address_attributes(aid, street_address, city, country, zip_code, senate_region, latitud, longitud)
                    return jsonify(Address=result), 201
                else:
                    return jsonify(Error="Attributes must not be null"), 400
            except:
                return jsonify(Error = 'Unexpected attributes in post request'), 400


    def updateAddress(self, aid, form):
        # dao = PartsDAO()
        # if not dao.getPartById(aid):
        #     return jsonify(Error = "Part not found."), 404
        # else:
            if len(form) != 7:
                return jsonify(Error="Malformed update request"), 400
            else:
                try:
                    street_address = form['street_address']
                    city = form['city']
                    country = form['country']
                    zip_code = form['zip_code']
                    senate_region = form['senate_region']
                    latitud = form['latitud']
                    longitud = form['longitud']
                    if street_address and city and country and zip_code and senate_region and latitud and longitud:
                        # dao.update(aid, parent_Address, name)
                        result = self.__build_address_attributes(aid, street_address, city, country, zip_code, senate_region, latitud, longitud)
                        return jsonify(Address=result), 200
                    else:
                        return jsonify(Error="Attributes must not be null"), 400
                except:
                    return jsonify(Error = 'Unexpected attributes in put request'), 400


    def deleteAddress(self, aid):
        #dao = PartsDAO()
        # if not dao.getPartById(aid):
        #     return jsonify(Error = "Part not found."), 404
        # else:
            # dao.delete(aid)
        return jsonify(DeleteStatus = "OK"), 200
