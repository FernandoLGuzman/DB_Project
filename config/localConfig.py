import os

mysql = {}

try:
    host = os.environ['host']
    username = os.environ['username']
    password = os.environ['password']
    database = os.environ['database']

    mysql['host'] = host
    mysql['username'] = username
    mysql['password'] = password
    mysql['database'] = database
    
except:
    mysql = {
        "host": "localhost",
        "username": "project-user",
        "password": "CIIC-4060",
        "database": "disaster_project"
    }