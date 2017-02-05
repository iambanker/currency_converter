import pytest
import tempfile
import json
from app.utils import prep_response, convert_amount, InternalError, get_curr_db


def test_response_template():
    response = prep_response()
    assert "result" in response
    assert "error" in response


@pytest.mark.parametrize(["amount", "curr_from", "curr_to"], [(100, "EUR", "CZK"), (100, "EUR", "USD"), (100, "CZK", "USD"), (1, "EUR", "PLN"), (10, "PLN", "CZK")])
def test_convert_amount(amount, curr_from, curr_to):
    result = convert_amount(amount, curr_from, curr_to)
    assert isinstance(result, dict)
    assert isinstance(result["amount_from"], float)
    assert isinstance(result["amount_to"], float)
    assert isinstance(result["curr_rate"], float)
    assert isinstance(result["curr_from"], str)
    assert isinstance(result["curr_to"], str)


@pytest.mark.parametrize(["amount", "curr_from", "curr_to"], [("asdf", "EUR", "CZK"), (100, "AAA", "USD"), (100, "CZK", "AAA")])
def test_convert_amount_exceptions(amount, curr_from, curr_to):
    try:
        convert_amount(amount, curr_from, curr_to)
        assert False
    except Exception:
        assert True


def test_internal_error():
    assert InternalError is not None


def test_curr_db():
    curr_db = get_curr_db()
    assert isinstance(curr_db, dict)
    try:
        curr_db = get_curr_db("wrong_db_path")
        assert False
    except InternalError:
        assert True
    fake_db = tempfile.NamedTemporaryFile(dir="/tmp")
    try:
        curr_db = get_curr_db(fake_db.name)
        assert False
    except InternalError:
        assert True
    fake_db = tempfile.NamedTemporaryFile(dir="/tmp", mode="w")
    fake_db.write(json.dumps({"fake": "db"}))
    try:
        curr_db = get_curr_db(fake_db.name)
        assert False
    except InternalError:
        assert True
