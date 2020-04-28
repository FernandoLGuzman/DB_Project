from flask import Flask
from routes.resources import resources
from routes.users import users
from routes.categories import categories
from routes.roles import roles

from flask_cors import CORS, cross_origin

import dao.connection

app = Flask(__name__)

CORS(app)

app.register_blueprint(resources, url_prefix='/resource')
app.register_blueprint(users, url_prefix='/user')
app.register_blueprint(categories, url_prefix='/category')
app.register_blueprint(roles, url_prefix='/role')

@app.route('/')
def hello_world():
    return 'Welcome to our DB project'
