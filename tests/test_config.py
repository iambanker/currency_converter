import json
import pytest


@pytest.fixture
def config():
    config_path = "conf/config.json"
    with open(config_path) as f:
        config_file = json.load(f)
    return config_file


def test_config_load(config):
    assert config is not None
    assert isinstance(config, dict)


def test_db_path(config):
    assert "DB_PATH" in config
    assert isinstance(config["DB_PATH"], str)


def test_fxopen_url(config):
    assert "OPENFX_URL" in config
    assert isinstance(config["OPENFX_URL"], str)


def test_fxopen_key(config):
    assert "OPENFX_KEY" in config
    assert isinstance(config["OPENFX_KEY"], str)


def test_update_interval(config):
    assert "UPDATE_INTERVAL" in config
    assert isinstance(config["UPDATE_INTERVAL"], float) or isinstance(config["UPDATE_INTERVAL"], int)
