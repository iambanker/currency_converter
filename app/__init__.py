from flask import Flask
from flask_cors import CORS
from .utils import api_logger


def create_app(config_filename=None):
    app = Flask(__name__)
    CORS(app)

    from .docs import auto
    auto.init_app(app)

    if config_filename:
        app.config.from_pyfile(config_filename)

    app.logger.addHandler(api_logger)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .docs import doc as doc_blueprint
    app.register_blueprint(doc_blueprint, url_prefix="/docs")

    from .api_1_0 import api as api_1_0_blueprint
    app.register_blueprint(api_1_0_blueprint, url_prefix="/api/v1.0")

    return app
