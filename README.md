# Currency convertor

Web service for conversion between currencies implemented in [flask](http://flask.pocoo.org).

* v0.1
* Python 3.5.2

## Setup

Clone repo and then run

```
virtualenv -p python3 venv # create separate environment
source venv/bin/activate # activate it

pip install -r conf/requirements.txt # install dependencies

cp conf/sample_config.json conf/config.json # create config file

python -m pytest tests # run test to check if everything is setup correctly
```

In case you want to update currency rates periodically register at [openexchangerates.org](https://openexchangerates.org) and change your API key in `config.json`:

```
{
  "OPENFX_URL": "https://openexchangerates.org/api/latest.json?app_id=",
  "OPENFX_KEY": "insert_your_api_key",
  "UPDATE_INTERVAL": 86400,
  ...
}
```

and run

```
python db/db_manager.py & # run as background service
```

`UPDATE_INTERVAL` specifies how often rates should be updated, default is every 24 hours.

## Example

Initiate multiple workers

```
gunicorn manager:app -w 4
```

and API is available at `127.0.0.1:8000`

To see implemented methods check docs `127.0.0.1:8000/docs`. All API calls return JSON in format

```
error: human readable error of api call if failed, empty list otherwise
result: contains result of api call if successful, empty list otherwise
```

* Get list of available currencies

```
curl -i http://127.0.0.1:8000/api/v1.0/currency

----

HTTP/1.1 200 OK
Server: gunicorn/19.6.0
Date: Fri, 03 Feb 2017 17:56:43 GMT
Connection: close
Content-Type: application/json
Access-Control-Allow-Origin: *
Content-Length: 50

{
  "error": [],
  "result": {
    "currency": [
      "XPT",
      "CDF",
      "PKR",
      "WST",
      "TZS",
      ...
      ]
    }
}
```

* Convert 100 EUR to CZK

```
curl -i http://127.0.0.1:8000/api/v1.0/convert?amount=100&curr_from=EUR&curr_to=CZK

----

HTTP/1.1 200 OK
Server: gunicorn/19.6.0
Date: Sun, 05 Feb 2017 17:37:36 GMT
Connection: close
Content-Type: application/json
Access-Control-Allow-Origin: *
Content-Length: 163

{
  "error": [],
  "result": {
    "amount_from": 100.0,
    "amount_to": 2702.6,
    "curr_from": "EUR",
    "curr_rate": 27.026,
    "curr_to": "CZK"
  }
}
```


## Todos

* write more tests
* change auto-documentation from `flask-autodoc`, candidate solution [Swagger](https://github.com/rantav/flask-restful-swagger)
* use some in-memory database like `Redis` instead of raw file to store currency rates
* add authentication
* improve logging features
* improve app configuration
