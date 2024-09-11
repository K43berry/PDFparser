from flask import Blueprint, request, jsonify
from models import db, User, RegexPattern

service_bp = Blueprint('service', __name__)

@service_bp.route('/newRegex', methods=["POST"])
def newRegex():
    rq_data = request.get_json()

    new_regex = RegexPattern(
        id = "id"
    )



