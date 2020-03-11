from flask import Flask
from routes.resources import resources
from routes.users import users

app = Flask(__name__)
app.register_blueprint(resources, url_prefix='/resource')
app.register_blueprint(users, url_prefix='/user')

@app.route('/')
def hello_world():
    return 'Welcome to our DB project'