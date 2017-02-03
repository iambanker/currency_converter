from flask import make_response, jsonify
from . import main


@main.app_errorhandler(404)
def not_found(e):
    return make_response(jsonify({'error': 'Not found'}), 404)


@main.app_errorhandler(405)
def not_implemented(e):
    return make_response(jsonify({'error': 'Not implemented'}), 405)
