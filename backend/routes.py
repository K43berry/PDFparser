from flask import Blueprint, request

routes_blueprint = Blueprint('routes', __name__)

@routes_blueprint.route('/')
def hello():
    return "Hello World"