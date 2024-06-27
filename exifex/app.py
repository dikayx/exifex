import logging
import sys

from flask import Flask

from exifex import routes
from exifex.config import Config


def create_app():
    """
    Create application factory, as explained here:
    http://flask.pocoo.org/docs/patterns/appfactories/.
    """
    app = Flask(__name__)
    app.config.from_object(Config)
    Config.init_app(app)

    register_blueprints(app)

    return app

def register_blueprints(app):
    """Register Flask blueprints."""
    app.register_blueprint(routes.blueprint)

def configure_logger(app):
    """Configure loggers."""
    handler = logging.StreamHandler(sys.stdout)
    if not app.logger.handlers:
        app.logger.addHandler(handler)
