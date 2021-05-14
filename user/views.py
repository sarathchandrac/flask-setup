from flask import Blueprint, Flask
from flask_restful import Api, Resource

# app = Flask(__name__)
# api_bp = Blueprint('api', __name__)
# api = Api(api_bp)
# user_app = Blueprint('user_app', __name__)
# api = Blueprint('api', __name__)

# @user_app.route('/login')
# def login():
#     return "user login"


class Login(Resource):
    def get(self):
        return {'result': 'Login!"'}


# api.add_resource(Login, '/login')