import requests
import json
import time


def update_currency_rates(config_filename="conf/config.json"):
    """
    Periodically update curreny rates in database
    """
    with open(config_filename) as f:
        config = json.load(f)
    API_URL = config["OPENFX_URL"]
    API_KEY = config["OPENFX_KEY"]
    UPDATE_INTERVAL = config["UPDATE_INTERVAL"]
    DB_PATH = config["DB_PATH"]
    rates_url = "{0}{1}".format(API_URL, API_KEY)

    while True:
        reply = requests.get(rates_url)
        try:
            reply.raise_for_status()
        except requests.exceptions.HTTPError as e:
            print("Currency rates were not updated {0}: {1}".format(time.ctime(), e.args))
            time.sleep(60)
            continue
        db = reply.json()
        with open(DB_PATH, "w") as conn:
            json.dump(db, conn)
        print("Currency rates updated {0}".format(time.ctime()))
        time.sleep(UPDATE_INTERVAL)


def main():
    update_currency_rates()


if __name__ == "__main__":
    main()
