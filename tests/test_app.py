import pytest
import json
from app import create_app


@pytest.fixture
def testapp():
    app = create_app()
    app.config['TESTING'] = True
    return app.test_client()


def test_docs_endpoint(testapp):
    resp = testapp.get('/docs', follow_redirects=True)
    assert "Documentation" in resp.data.decode("utf-8")


def test_currency_endpoint(testapp):
    resp = testapp.get('/api/v1.0/currency')
    data = json.loads(resp.data.decode("utf-8"))
    assert "result" in data
    assert "error" in data
    assert isinstance(data["result"]["currency"], list)
    supported_currencies = ["CZK", "USD", "EUR", "PLN"]
    for currency in supported_currencies:
        assert currency in data["result"]["currency"]


@pytest.mark.parametrize(["amount", "curr_from", "curr_to"], [(100, "EUR", "CZK"), (100, "EUR", "USD"), (100, "CZK", "USD"), (1, "EUR", "PLN"), (10, "PLN", "CZK")])
def test_convert_endpoint(testapp, amount, curr_from, curr_to):
    api_url = '/api/v1.0/convert?amount={0}&curr_from={1}&curr_to={2}'.format(amount, curr_from, curr_to)
    resp = testapp.get(api_url)
    data = json.loads(resp.data.decode("utf-8"))
    assert "result" in data
    assert "error" in data
    assert isinstance(data["result"]["amount_from"], float)
    assert isinstance(data["result"]["amount_to"], float)
    assert isinstance(data["result"]["curr_rate"], float)
    assert isinstance(data["result"]["curr_from"], str)
    assert isinstance(data["result"]["curr_to"], str)


def test_api_return_codes(testapp):
    # home url is not implemented
    resp = testapp.get('/')
    assert resp.status_code == 404
    # documentation should be found at /docs
    resp = testapp.get('/docs')
    assert resp.status_code == 301
    # currency method support only get method
    resp = testapp.get('/api/v1.0/currency')
    assert resp.status_code == 200
    resp = testapp.post('/api/v1.0/currency')
    assert resp.status_code == 405
    resp = testapp.delete('/api/v1.0/currency')
    assert resp.status_code == 405
    resp = testapp.put('/api/v1.0/currency')
    assert resp.status_code == 405
    # convert method support only get method
    resp = testapp.get('/api/v1.0/convert?amount=1&curr_from=CZK&curr_to=EUR')
    assert resp.status_code == 200
    resp = testapp.get(
        '/api/v1.0/convert?amount=asdf&curr_from=CZK&curr_to=EUR')
    assert resp.status_code == 400
    resp = testapp.get('/api/v1.0/convert?amount=1&curr_from=AAA&curr_to=EUR')
    assert resp.status_code == 400
    resp = testapp.get('/api/v1.0/convert?amount=1&curr_from=CZK&curr_to=AAA')
    assert resp.status_code == 400
    resp = testapp.post('/api/v1.0/convert')
    assert resp.status_code == 405
    resp = testapp.delete('/api/v1.0/convert')
    assert resp.status_code == 405
    resp = testapp.put('/api/v1.0/convert')
    assert resp.status_code == 405
