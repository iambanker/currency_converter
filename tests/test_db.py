import pytest
import json


@pytest.fixture
def config():
    config_path = "conf/config.json"
    with open(config_path) as f:
        config_file = json.load(f)
    return config_file


def test_db_load(config):
    db_path = config["DB_PATH"]
    with open(db_path) as conn:
        db = json.load(conn)
    assert db is not None
