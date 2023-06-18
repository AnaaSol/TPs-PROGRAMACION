from modules.config import db
from sqlalchemy import Column, Integer, String, Float, ForeignKey 
from flask_login import UserMixin

class Boss(db.Model):
    __tablename__ = 'jefes'
    id = Column(Integer(), primary_key=True)
    nombre = Column(String(1000), nullable=False, unique=True)
    autor = Column(String(1000), nullable=False)
    user_id = Column(Integer(), ForeignKey('users.id'))

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = Column(Integer(), primary_key=True)
    email = Column(String(100), unique=True)
    user = Column(String(100), unique=True)
    password = Column(String(100))
    name = Column(String(1000))
    surname= Column(String(1000))