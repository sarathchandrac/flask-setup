from flask import Flask
from flask_restful import Api
from flask_bootstrap import Bootstrap
from routes import api, api_bp

bootstrap = Bootstrap()


def create_app():

    app = Flask(__name__)
    # app.config.from_object(config[config_name])
    # config[config_name].init_app(app)
    app.config.from_pyfile('settings.py')
    # print("config", app.config.get('SECRET_KEY'))

    # bootstrap.init_app(app)

    app.register_blueprint(api_bp)

    return app
