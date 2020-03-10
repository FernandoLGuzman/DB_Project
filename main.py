from flask import Flask
from routes.resources import resources

app = Flask(__name__)
app.register_blueprint(resources, url_prefix='/resource')

@app.route('/')
def hello_world():
    return 'Hello, World!'