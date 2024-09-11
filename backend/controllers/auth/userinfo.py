import os
import requests
from flask import request, jsonify


def getUserInfo():
    jwt_token = request.headers.get('Authorization')

    headers = {
        'Authorization': jwt_token,
        'apikey': os.getenv('SUPABASE_AUTH_KEY') 
    }
    try:
        response = requests.get(os.getenv('SUPABASE_AUTH_URI') + '/auth/v1/user', headers=headers)
        data = response.json()
        return data.get('identities', [])[0].get('identity_data', {})
    except requests.exceptions.RequestException as e:
        return jsonify({"message": "Error! Connection with DB failed"}), 401