__author__ = 'alair.tavares'

from flask import Flask
from pymongo import MongoClient

uri = "mongodb://$OPENSHIFT_MONGODB_DB_HOST:$OPENSHIFT_MONGODB_DB_PORT"
#uri = "mongodb://localhost:27017"
client = MongoClient(uri)
db = client['pfmoo']
#for mongodb on opensfhit
db.authenticate('admin', 'CK5s3mNkuwfb')

app = Flask(__name__)

from app.resources import __init__