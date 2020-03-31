from flask import Blueprint, request, jsonify
from handlers.categoryHandler import CategoryHandler

categories = Blueprint('categories', __name__)

@categories.route('/', methods = ['GET', 'POST'])
def category():
    if request.method == 'GET':
        #GET handle rcode
        return CategoryHandler().getAllCategories()
    elif request.method == 'POST':
        #POST handler code
        print("REQUEST: ", request.json)
        return CategoryHandler().insertCategory(request.json)

@categories.route('/<int:id>', methods = ['GET', 'PUT', 'DELETE'])
def categoryById(id):
    if request.method == 'GET':
        #GET handler code
        return CategoryHandler().getCategoryById(id)
    elif request.method == 'PUT':
        #PUT handler code
        return CategoryHandler().updateCategory(id, request.json)
    elif request.method == 'DELETE':
        #DELETE handler code
        return CategoryHandler().deleteCategory(id)
