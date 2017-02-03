import json

def test_fxopen_key():
    with open("conf/config.json") as f:
        config = json.load(f)
    assert "OPENFX_KEY" in config
    assert len(config["OPENFX_KEY"]) > 0
