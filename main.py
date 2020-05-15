from flask import Flask
from routes.resources import resources
from routes.users import users
from routes.categories import categories
from routes.roles import roles
from routes.requests import requests
from routes.purchases import purchases
from routes.senate_regions import regions
from routes.addresses import addresses
from routes.payments import payments

from flask_cors import CORS, cross_origin

app = Flask(__name__)

CORS(app)

app.register_blueprint(resources, url_prefix='/resource')
app.register_blueprint(users, url_prefix='/user')
app.register_blueprint(categories, url_prefix='/category')
app.register_blueprint(roles, url_prefix='/role')
app.register_blueprint(requests, url_prefix='/request')
app.register_blueprint(purchases, url_prefix='/purchase')
app.register_blueprint(regions, url_prefix='/regions')
app.register_blueprint(addresses, url_prefix='/address')
app.register_blueprint(payments, url_prefix='/paymentMethod')

@app.route('/')
def hello_world():
    return 'Welcome to our DB project'
