from modulos.config import db
#from sqlalchemy import Column, Integer, String, ForeignKey, ARRAY
from flask_login import UserMixin
from abc import ABC, abstractmethod
import datetime

class Persona(ABC, db.Model):
    #@abstractmethod; ¿por qué habría de ser un método abstracto si la implementación en las clases hijas es la misma?
    def __init__(self):
        __email = db.Column(db.String(100), unique=True, nullable=False)
        __user_name = db.Column(db.String(100), unique=True, nullable=False)
        __password = db.Column(db.String(100), nullable=False)
        __name = db.Column(db.String(100), nullable=False)
        __surname= db.Column(db.String(100), nullable=False)

    def set_nombre(self, nombre):
        self.__nombre=nombre
    
    def get_nombre(self):
        return self.__nombre

    def set_apellido(self, apellido):
        self.__apellido=apellido
    
    def get_apellido(self):
        return self.__apellido
    
    def set_usuario(self, usuario):
        #añadir control de que el nuevo usuario sea único
        self.__usuario=usuario
    
    def get_usuario(self):
        return self.__usuario

    def set_contraseña(self, contraseña):
        self.__contraseña=contraseña
    
    def get_contraseña(self):
        return self.__contraseña

    def set_mail(self, mail):
        #añadir control de que el nuevo mail sea único
        self.__mail=mail
    
    def get_mail(self):
        return self.__mail
    
    # ¿se debería poder cambiar el claustro una vez creada la cuenta?
    # def set_claustro(self, claustro):
    #     self.__claustro=claustro
        
    def set_claustro(self):
        return self.__claustro
    
    def cambiar_contraseña(self, contraseña, contraseña_nueva):
        if contraseña==self.__contraseña:
            self.__contraseña=contraseña_nueva
        else:
            return "La contraseña ingresada no coincide."

class Jefe(Persona, UserMixin, db.Model):

    def __init__(self):
        __tablename__ = 'jefes'
        __depto = db.Column(db.String(100), primary_key=True)

    def actualizar_estado(self):
        pass
    
    def derivar_reclamo(self):
        pass

    def generar_reporte(self):
        pass

class Usuario(Persona, UserMixin, db.Model):

    def __init__(self):
        __tablename__ = 'users'
        __claustro = db.Column(db.String(100), nullable=False)
        __id = db.Column(db.Integer(), primary_key=True)
        __reclamos_adheridos = db.Column(db.ARRAY())
        __reclamos_generados = db.Column(db.ARRAY())
    
    def generar_reclamo(self, nombre_reclamo, descripcion):
        reclamo=[nombre_reclamo, descripcion, "(datetime.datetime.now())[:19]"]
        self.__reclamos_generados.append(reclamo)
        return reclamo #reclamo tiene la información necesaria para crear un objeto reclamo
    
    def adherirse_a_reclamo(self, nombre_reclamo):
        self.__reclamos_adheridos.append(nombre_reclamo)

class Reclamo(db.Model):
    __tablename__='reclamos'
    reclamo_id = db.Column(db.Integer(), db.ForeignKey('recl.id'))
    __description = db.Column(db.String(10000), nullable=False)
    __estado = db.Column(db.String())
    __depto = db.Column(db.String())
    __fecha_hora = db.Column(db.String())
    __numero_de_adherentes = db.Column(db.String())
    __title = db.Column(db.String(100), nullable=False)
    __id_user = db.Column(db.Integer(), db.ForeignKey('users.id'))

    def contar_adherentes(self):
        pass
