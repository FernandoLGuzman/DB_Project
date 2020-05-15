from flask import jsonify
from dao.category import CategoryDao

class CategoryHandler:
    def __build_category_dict(self, row):
        result = {}
        result['category_id'] = row[0]
        result['parent_category'] = row[2]
        result['category_name'] = row[1]
        return result


    def __build_category_attributes(self, category_id, parent_category, name):
        result = {}
        result['category_id'] = category_id
        result['parent_category'] = parent_category
        result['name'] = name
        return result


    def getAllCategories(self):
        dao = CategoryDao()
        categories_list = dao.getAllCategories()
        result_list = []
        for row in categories_list:
            result = self.__build_category_dict(row)
            result_list.append(result)
        return jsonify(Categories = result_list), 200


    def getCategoryById(self, cid):
        dao = CategoryDao()
        row = dao.getCategoryByID(cid)
        if not row:
            return jsonify(Error = "Category Not Found"), 404
        else:
            result = self.__build_category_dict(row)
            return jsonify(Category = result), 200


    def insertCategory(self, form):
        if not form:
            return jsonify(Error = "empty form"), 400
        print("form: ", form)
        if len(form) != 2:
            return jsonify(Error = "Malformed post request"), 400
        else:
            try:
                parent_category = form['parent_category']
                name = form['name']
                if name:
                    dao = CategoryDao()
                    cid = dao.insert(name,parent_category)
                    result = self.__build_category_attributes(cid, parent_category, name)
                    return jsonify(Category=result), 201
                else:
                    return jsonify(Error="Attributes must not be null"), 400
            except:
                return jsonify(Error = 'Unexpected attributes in post request'), 400


    def updateCategory(self, cid, form):
        # dao = PartsDAO()
        # if not dao.getPartById(cid):
        #     return jsonify(Error = "Part not found."), 404
        # else:
            if len(form) != 2:
                return jsonify(Error="Malformed update request"), 400
            else:
                try:
                    parent_category = form['parent_category']
                    name = form['name']
                    if name:
                        # dao.update(cid, parent_category, name)
                        result = self.__build_category_attributes(cid, parent_category, name)
                        return jsonify(Category=result), 200
                    else:
                        return jsonify(Error="Attributes must not be null"), 400
                except:
                    return jsonify(Error = 'Unexpected attributes in put request'), 400


    def deleteCategory(self, cid):
        #dao = PartsDAO()
        # if not dao.getPartById(cid):
        #     return jsonify(Error = "Part not found."), 404
        # else:
            # dao.delete(cid)
        return jsonify(DeleteStatus = "OK"), 200
