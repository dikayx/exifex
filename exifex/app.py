import logging
import sys

from flask import Flask

from exifex.config import Config
from exifex.routes import blueprint


def create_app():
    """
    Create application factory, as explained here:
    http://flask.pocoo.org/docs/patterns/appfactories/.
    :param config_object: The configuration object to use.
    """
    app = Flask(__name__)
    app.config.from_object(Config)
    Config.init_app(app)

    register_blueprints(app)

    return app

def register_blueprints(app):
    """Register Flask blueprints."""
    app.register_blueprint(blueprint)

def configure_logger(app):
    """Configure loggers."""
    handler = logging.StreamHandler(sys.stdout)
    if not app.logger.handlers:
        app.logger.addHandler(handler)
