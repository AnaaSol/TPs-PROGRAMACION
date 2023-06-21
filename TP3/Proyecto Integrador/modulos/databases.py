from modulos.config import db
from sqlalchemy import Column, Integer, String, ForeignKey, ARRAY
from flask_login import UserMixin
from abc import ABC, abstractmethod
import datetime

class Persona(ABC):
    @abstractmethod
    def __init__(self):
        self.__email = Column(String(100), unique=True, nullable=False)
        self.__claustr = Column(String(100), nullable=False)
        self.__user_name = Column(String(100), unique=True, nullable=False)
        self.__password = Column(String(100), nullable=False)
        self.__name = Column(String(100), nullable=False)
        self.__surname= Column(String(100), nullable=False)

class Jefe(Persona, UserMixin, db.Model):
    def __init__(self):
        self.__tablename__ = 'jefes'
        self.__depto = Column(String(100), primary_key=True)

    def actualizar_estado(self):
        pass
    
    def derivar_reclamo(self):
        pass

    def generar_reporte(self):
        pass

class User(Persona, UserMixin, db.Model):
    def __init__(self):
        self.__tablename__ = 'users'
        self.__id = Column(Integer(), primary_key=True)
        self.__reclamos_adheridos = Column(ARRAY())
        self.__reclamos_generados = Column(ARRAY())
    
    def generar_reclamo(self, nombre_reclamo, descripcion):
        self.__reclamos_generados.append([nombre_reclamo, descripcion, (datetime.datetime.now())[:19]])
        reclamo=[nombre_reclamo, descripcion, (datetime.datetime.now())[:19]]
        return reclamo
    
    def adherirse_a_reclamo(self, nombre_reclamo):
        self.__reclamos_adheridos.append(nombre_reclamo)

class Claim(db.Model):
    __tablename__='reclamo'
    recl_id = Column(Integer(), ForeignKey('recl.id'))
    description = Column(String(10000), nullable=False)
    estado = Column(String())
    depto = Column(String())
    fecha_hora = Column(String())
    numero_de_adherentes = Column(String())
    title = Column(String(100), nullable=False)
    id_user = Column(Integer(), ForeignKey('users.id'))

    def contar_adherentes(self):
        pass
