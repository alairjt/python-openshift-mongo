__author__ = 'alair.tavares'

from app import app
from flask import make_response, jsonify

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found (PFMoO)'}), 404)

@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify({'Erro': 'Bad Request (PFMoO)'}), 400)

