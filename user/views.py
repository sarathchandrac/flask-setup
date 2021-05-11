from flask import Blueprint, Flask
from flask_restful import Resource


class Login(Resource):
    def get(self):
        return "Login"
    