import json
import logging

# import config
with open("conf/config.json") as f:
    config = json.load(f)

# Create api_logger
api_logger = logging.getLogger("API_logger")
sh = logging.StreamHandler()
sh.setFormatter(logging.Formatter(
    '[%(asctime)s] [%(process)d] [%(levelname)s] %(message)s '
    '[in %(pathname)s:%(lineno)d]'
))
api_logger.addHandler(sh)


# Custom exception for handling internal errors
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
        amount = round(float(amount), 2)
    except ValueError:
        raise Exception(
            "specified amount <{0}> is not float type".format(amount))
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


def get_curr_db(db_path=None):
    """
    Return dict of currency rates from currency database.
    """
    if not db_path:
        db_path = config["DB_PATH"]
    try:
        with open(db_path) as conn:
            db = json.load(conn)
        curr_db = db["rates"]
    except FileNotFoundError:
        raise InternalError("Database couldn't be loaded")
    except json.decoder.JSONDecodeError:
        raise InternalError("Database is not a JSON format")
    except KeyError:
        raise InternalError("Currency database is not available")

    return curr_db
