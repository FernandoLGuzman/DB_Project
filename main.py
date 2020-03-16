from flask import Flask
from routes.resources import resources
from routes.categories import categories
from routes.roles import roles

app = Flask(__name__)
app.register_blueprint(resources, url_prefix='/resource')
app.register_blueprint(categories, url_prefix='/category')
app.register_blueprint(roles, url_prefix='/role')

@app.route('/')
def hello_world():
    return 'Hello, World!'