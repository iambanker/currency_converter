from flask import make_response, jsonify
from . import main
from ..utils import prep_response


@main.app_errorhandler(400)
def bad_request(e):
    resp = prep_response()
    resp["error"] = e.description['message']
    return make_response(jsonify(resp), 400)


@main.app_errorhandler(404)
def not_found(e):
    resp = prep_response()
    resp["error"] = "Not found!"
    return make_response(jsonify(resp), 404)


@main.app_errorhandler(405)
def not_implemented(e):
    resp = prep_response()
    resp["error"] = "Not implemented!"
    return make_response(jsonify(resp), 405)


@main.app_errorhandler(500)
def internal_error(e):
    resp = prep_response()
    resp["error"] = "Sorry, something went wrong on our side but it will be fixed soon!"
    return make_response(jsonify(resp), 500)
