from modulos.persona import Persona
from flask_login import UserMixin
from modulos.config import db

class Jefe(Persona, UserMixin, db.Model):

    __tablename__ = 'jefes'

    __depto = db.Column(db.String(100), primary_key=True) #vendría a ser el ID

    def actualizar_estado(self):
        pass
    
    def derivar_reclamo(self):
        pass

    def generar_reporte(self):
        pass