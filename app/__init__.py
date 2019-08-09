"""
    create by Gray 2019-07-08
"""
from .app import Flask


def register_blueprints(flask_app):
    from app.api.v1 import create_blueprint_v1
    flask_app.register_blueprint(create_blueprint_v1(), url_prefix='/v1')


def register_plugin(flask_app):
    from app.models.base import db
    db.init_app(flask_app)
    with flask_app.app_context():
        db.create_all()


def create_app():
    flask_app = Flask(__name__)
    flask_app.config.from_object('app.config.setting')
    flask_app.config.from_object('app.config.secure')

    register_blueprints(flask_app)
    register_plugin(flask_app)

    return flask_app
