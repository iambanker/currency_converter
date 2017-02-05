import json


class InternalError(Exception):
    pass


def prep_response():
    """
    Return base dict template which is used to create responses.
    """
    return {"error": [], "result": []}


def convert_amount(amount, curr_from, curr_to):
    """
    Return converted amount in curr_to calculated from amount in  curr_from

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
    try:
        amount = float(amount)
    except ValueError:
        raise Exception("specified amount <{0}> is not float type".format(amount))
    curr_db = get_curr_db()
    rate_from = curr_db.get(curr_from, None)
    if not rate_from:
        raise Exception("<{0}> is not supported currency".format(curr_from))
    rate_to = curr_db.get(curr_to, None)
    if not rate_to:
        raise Exception("<{0}> is not supported currency".format(curr_to))

    curr_rate = round(rate_to / rate_from, 3)
    amount_to = round(amount * curr_rate, 2)
    result = {
        "amount_from": amount,
        "amount_to": amount_to,
        "curr_from": curr_from,
        "curr_to": curr_to,
        "curr_rate": curr_rate,
    }
    return result


def get_curr_db():
    """
    Return dict of currency rates from currency database.
    """
    try:
        with open("db/latest.json") as conn:
            db = json.load(conn)
        curr_db = db["rates"]
    except FileNotFoundError:
        raise InternalError("Database couldn't be loaded")
    except KeyError:
        raise InternalError("Currency database is not available")

    return curr_db
