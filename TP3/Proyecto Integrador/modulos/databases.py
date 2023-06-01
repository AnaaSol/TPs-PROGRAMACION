# from modules.config import db
# from sqlalchemy import Column, Integer, String, Float, ForeignKey 
# from flask_login import UserMixin
# #https://docs.sqlalchemy.org/en/13/orm/basic_relationships.html

# class User(UserMixin, db.Model):
#     __tablename__ = 'users'
#     id = Column(Integer(), primary_key=True)
#     email = Column(String(100), unique=True)
#     password = Column(String(100))
#     name = Column(String(1000))
#     user_name = Column(String(1000), unique=True)
#     surname = Column(String(1000))
#     email = Column(String(10000), unique=True)