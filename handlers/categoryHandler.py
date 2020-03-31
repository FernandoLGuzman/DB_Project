from flask import jsonify
class CategoryHandler:
    def __build_category_dict(self, row):
        result = {}
        result['category_id'] = row[0]
        result['parent_category'] = row[1]
        result['name'] = row[2]
        return result


    def __build_category_attributes(self, category_id, parent_category, name):
        result = {}
        result['category_id'] = category_id
        result['parent_category'] = parent_category
        result['name'] = name
        return result


    def getAllCategories(self):
        #dao = PartsDAO()
        categories_list = [[0, None, 'category'], [1, 0, 'category2']]
        #categories_list = dao.getAllParts()
        result_list = []
        for row in categories_list:
            result = self.__build_category_dict(row)
            result_list.append(result)
        return jsonify(Categories = result_list), 200


    def getCategoryById(self, pid):
        categories_list = [[pid, 'null', 'category']]
        result_list = []
        for row in categories_list:
            result = self.__build_category_dict(row)
            result_list.append(result)
        return jsonify(Category = result_list), 200


    def insertCategory(self, form):
        if not form:
            return jsonify(Error = "empty form"), 400
        print("form: ", form)
        if len(form) != 2:
            return jsonify(Error = "Malformed post request"), 400
        else:
            parent_category = form['parent_category']
            name = form['name']
            if name:
                #dao = PartsDAO()
                pid = 0
                #pid = dao.insert(parent_category, name)
                result = self.__build_category_attributes(pid, parent_category, name)
                return jsonify(Category=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400


    def updateCategory(self, pid, form):
        # dao = PartsDAO()
        # if not dao.getPartById(pid):
        #     return jsonify(Error = "Part not found."), 404
        # else:
            if len(form) != 2:
                return jsonify(Error="Malformed update request"), 400
            else:
                parent_category = form['parent_category']
                name = form['name']
                if name:
                    # dao.update(pid, parent_category, name)
                    result = self.__build_category_attributes(pid, parent_category, name)
                    return jsonify(Category=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400


    def deleteCategory(self, pid):
        #dao = PartsDAO()
        # if not dao.getPartById(pid):
        #     return jsonify(Error = "Part not found."), 404
        # else:
            # dao.delete(pid)
        return jsonify(DeleteStatus = "OK"), 200
