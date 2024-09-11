from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, UUID, String

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id = Column(UUID(as_uuid=True), primary_key=True, nullable=False)
    email = Column(String(254), unique=True, nullable=False)

class RegexPattern(db.Model):
    __tablename__ = 'regex_pattern'
    id = Column(UUID(as_uuid=True), primary_key=True, nullable=False)
    user_id = Column(UUID(as_uuid=True), primary_key = True, nullable=False)

    name = Column(String(50), unique=True, nullable=False)
    regex = Column(String(1000), unique=False, nullable=True)
