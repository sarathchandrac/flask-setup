from flask import Flask
from flask import Flask, Blueprint
from flask_restful import Api
from flask_bootstrap import Bootstrap
from user.views import Login

bootstrap = Bootstrap()
# api_bp = Blueprint('api', __name__)
# api = Api(api_bp)

# app = Flask(__name__)
api_bp = Blueprint('api', __name__)
api = Api(api_bp)


api.add_resource(Login, '/login')
