from flask import jsonify
from . import api


@api.route('/currency', methods=['GET'])
def currency():
    """
    Return list of available currencies.

    Input
    -----

    Return
    -----
    currency - array of available currencies
    """
    response = {"result": "Hello pairs!",
                "error": [], }
    return jsonify(response)


@api.route('/convert', methods=['POST'])
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
    response = {"result": "Hello converter!",
                "error": []}
    return jsonify(response)
