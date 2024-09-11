import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from flask_cors import CORS

from blueprints.service import service_bp
from blueprints.user import user_bp
from models import db

load_dotenv()

#=============================#
app = Flask(__name__)
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv('SUPABASE_CONNECTION_STRING')

db.init_app(app)

with app.app_context():
    db.create_all()

#=============================#

#BLUEPRINTS
app.register_blueprint(service_bp)
app.register_blueprint(user_bp)


#=============================#

if __name__ == "__main__":
    app.run(debug = True, port=8080)

#=============================#