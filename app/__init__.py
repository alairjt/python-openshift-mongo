__author__ = 'alair.tavares'

from flask import Flask
from pymongo import MongoClient

#uri = "mongodb://XXX.X.XXX.XXX:27017"
uri = "mongodb://localhost:27017"
client = MongoClient(uri)
db = client['pom']
#for mongodb on opensfhit
#db.authenticate('admin', 'XXXXXX')

app = Flask(__name__)

from app.resources import __init__