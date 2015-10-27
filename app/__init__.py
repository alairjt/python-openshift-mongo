__author__ = 'alair.tavares'

from flask import Flask
from pymongo import MongoClient

uri = "mongodb://$OPENSHIFT_MONGODB_DB_HOST:$OPENSHIFT_MONGODB_DB_PORT"
client = MongoClient(uri)
db = client['database']
#for mongodb on opensfhit
db.authenticate('admin', 'XXXXX')

app = Flask(__name__)

from app.resources import __init__