from functools import wraps
from flask import Blueprint, request, jsonify
from dotenv import load_dotenv

from models import db, User, RegexPattern
from controllers.auth.jwt import tokenReq
from controllers.auth.userinfo import getUserInfo

load_dotenv()

user_bp = Blueprint('user', __name__)

@user_bp.route('/register', methods=["POST"])
@tokenReq
def register():

    data = getUserInfo()

    new_user = User(
        id = data.get('sub', None),
        email = data.get('email', None)
    )

    try:
        db.session.add(new_user)
        db.session.commit()
    except Exception as err:
        return jsonify({"message": "Could not insert data into database"}), 400
    
    return {"message": "User created"}, 201