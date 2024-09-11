import os
import requests
from functools import wraps
from flask import request, jsonify

def tokenReq(f):
    @wraps(f)
    def tokenReq_dec(*args,**kwargs):

        jwt_token = request.headers.get('Authorization')

        headers = {
        'Authorization': jwt_token,
        'apikey': os.getenv('SUPABASE_AUTH_KEY') 
        }

        try:
            response = requests.get(os.getenv('SUPABASE_AUTH_URI') + '/auth/v1/user', headers=headers)
            
            if response.status_code == 200:
                data = response.json()
                if data.get('aud') == 'authenticated':
                    return f(*args, **kwargs)
                return jsonify({"message": "Invalid or outdated sesion. Please refresh the page."}), 401
            return jsonify({"message": "Error! No token detected"}), 401
        except requests.exceptions.RequestException as e:
            return jsonify({"message": "Error! Connection with DB failed"}), 401
    return tokenReq_dec
