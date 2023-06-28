from modulos.persona import Persona
from flask_login import UserMixin
from modulos.config import db

class Usuario(Persona, UserMixin, db.Model):
        
    __tablename__ = 'users'

    __claustro = db.Column(db.String(100), nullable=False)
    __ID_user = db.Column(db.Integer(), db.ForeignKey("personas.__ID"), primary_key=True)
    __reclamos_adheridos = db.Column(db.ARRAY())
    __reclamos_generados = db.Column(db.ARRAY())

    def set_claustro(self, claustro):
        self.__claustro=claustro

    def get_claustro(self):
        return self.__claustro
    
    def generar_reclamo(self, nombre_reclamo, descripcion):
        reclamo=[nombre_reclamo, descripcion, "(datetime.datetime.now())[:19]"]
        self.__reclamos_generados.append(reclamo)
        return reclamo #reclamo tiene la información necesaria para crear un objeto reclamo
    
    def adherirse_a_reclamo(self, nombre_reclamo):
        self.__reclamos_adheridos.append(nombre_reclamo)