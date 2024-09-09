import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

from routes import routes_blueprint
from models import db

load_dotenv()

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv('SUPABASE_CONNECTION_STRING')

db.init_app(app)

with app.app_context():
    db.create_all()

app.register_blueprint(routes_blueprint)

if __name__ == "__main__":
    app.run(debug = True)
