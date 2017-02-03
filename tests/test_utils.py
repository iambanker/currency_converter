from app.utils import prep_response


def test_response_template():
    response = prep_response()
    assert "result" in response
    assert "error" in response
