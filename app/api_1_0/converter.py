from flask import jsonify, request, abort
from . import api
from ..utils import prep_response, convert_amount, get_curr_db, InternalError
from ..docs import auto

# TODO: use logging


@api.route('/currency', methods=['GET'])
@auto.doc(groups="public")
def currency():
    """
    Return list of supported currencies.

    Input
    -----

    Return
    -----
    currency - array of supported currencies
    """
    try:
        curr_db = get_curr_db()
    except InternalError as e:
        print(e.args)
        abort(500)
    currency_list = list(curr_db.keys())
    resp = prep_response()
    resp["result"] = {"currency": currency_list}
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
    curr_rate - float, currency rate used to convert amount rounded to 3 decimal places
    curr_from - string, currency of amount_from
    curr_to - string, currency of amount_to
    """
    amount = request.args.get("amount", None)
    if not amount:
        abort(400, {"message": "<amount> is required argument"})
    curr_from = request.args.get("curr_from")
    if not curr_from:
        abort(400, {"message": "<curr_from> is required argument"})
    curr_to = request.args.get("curr_to")
    if not curr_to:
        abort(400, {"message": "<curr_to> is required argument"})

    try:
        resp = prep_response()
        result = convert_amount(amount, curr_from, curr_to)
        resp["result"] = result
        return jsonify(resp)
    except InternalError as e:
        print(e.args)
        abort(500)
    except Exception as e:
        abort(400, {"message": e.args[0]})
