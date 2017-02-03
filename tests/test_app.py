import pytest
import json
from app import create_app


@pytest.fixture
def testapp():
    app = create_app()
    app.config['TESTING'] = True
    return app.test_client()


def test_currency_endpoint(testapp):
    resp = testapp.get('/api/v1.0/currency')
    assert resp.status_code == 200
    data = json.loads(resp.data.decode("utf-8"))
    assert "result" in data
    assert "error" in data


def test_convert_endpoint(testapp):
    resp = testapp.get('/api/v1.0/convert')
    assert resp.status_code == 200
    data = json.loads(resp.data.decode("utf-8"))
    assert "result" in data
    assert "error" in data


def test_api_methods(testapp):
    resp = testapp.get('/api/v1.0/currency')
    assert resp.status_code == 200
    resp = testapp.post('/api/v1.0/currency')
    assert resp.status_code == 405
    resp = testapp.delete('/api/v1.0/currency')
    assert resp.status_code == 405
    resp = testapp.put('/api/v1.0/currency')
    assert resp.status_code == 405

    resp = testapp.get('/api/v1.0/convert')
    assert resp.status_code == 200
    resp = testapp.post('/api/v1.0/convert')
    assert resp.status_code == 405
    resp = testapp.delete('/api/v1.0/convert')
    assert resp.status_code == 405
    resp = testapp.put('/api/v1.0/convert')
    assert resp.status_code == 405
