__author__ = 'alair.tavares'

from flask import Flask
from pymongo import MongoClient

uri = "mongodb://127.6.16.130:27017"
#uri = "mongodb://localhost:27017"
client = MongoClient(uri)
db = client['pfmoo']
#for mongodb on opensfhit
db.authenticate('admin', 'CK5s3mNkuwfb')

app = Flask(__name__)

from app.resources import __init__