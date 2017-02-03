from flask import make_response, jsonify
from . import main
from ..utils import prep_response


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
