#from modulos.config import db #no encuentra modulos
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask("server")

app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

Bootstrap(app)
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)

class Reclamo(db.Model):

    __tablename__='reclamos'

    ID_reclamo = db.Column(db.Integer(), primary_key=True) #no los reconoce con doble guion bajo al principio
    description = db.Column(db.String(10000), nullable=False)
    estado = db.Column(db.String(10))
    depto = db.Column(db.String(25))
    timestap = db.Column(db.String(50))
    adherentes = db.Column(db.String())
    title = db.Column(db.String(100), nullable=False)
    id_user = db.Column(db.Integer(), db.ForeignKey('users.id'))

    #getters

    def get_ID(self):
        return self.ID_reclamo #somehow works

    def contar_adherentes(self):
        pass

nuevo_reclamo=Reclamo(
    ID_reclamo=90, 
    description="No hay papel higiénico en el módulo 1 durante toda la mañana", 
    estado="Pendiente", 
    depto="", 
    timestap="13/07/23", 
    adherentes="",
    title="Prueba", 
    id_user=92)
print(nuevo_reclamo.get_ID())