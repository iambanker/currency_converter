from flask import jsonify
from . import api
from ..utils import prep_response
from ..docs import auto

# TODO: use logging


@api.route('/currency', methods=['GET'])
@auto.doc(groups="public")
def currency():
    """
    Return list of available currencies.

    Input
    -----

    Return
    -----
    currency - array of available currencies
    """
    resp = prep_response()
    resp["result"] = "Hello currency!"
    return jsonify(resp)


@api.route('/convert', methods=['GET'])
@auto.doc(groups="public")
def convert():
    """
    Return converted amount to specified currency.

    Input
    -----
    amount - float, amount to convert
    curr_from - string, specify currency of amount
    curr_to - string, specify currency to which amount will be converted

    Return
    -----
    amount_from - float, amount in from currency rounded to 2 decimal places
    amount_to - float, amount in to currency rounded to 2 decimal places
    curr_from - string, currency of amount_from
    curr_to - string, currency of amount_to
    curr_rate - float, currency rate used to convert amount
    """
    resp = prep_response()
    resp["result"] = "Hello converter!"
    return jsonify(resp)
