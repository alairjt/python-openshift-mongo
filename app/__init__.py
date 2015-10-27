__author__ = 'alair.tavares'

from flask import Flask
from pymongo import MongoClient

uri = "mongodb://$OPENSHIFT_MONGODB_DB_HOST:$OPENSHIFT_MONGODB_DB_PORT"
#uri = "mongodb://127.6.16.XXX:27017"
client = MongoClient(uri)
db = client['database']
db.authenticate('admin', 'XXXX')

app = Flask(__name__)

from app.resources import __init__