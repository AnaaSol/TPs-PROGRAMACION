from abc import ABC
from modulos.config import db

class Persona(ABC, db.Model):

    __tablename__='personas'

    __email= db.Column(db.String(100), unique=True, nullable=False)
    __usuario= db.Column(db.String(100), unique=True, nullable=False)
    __contraseña= db.Column(db.String(100), nullable=False)
    __nombre= db.Column(db.String(100), nullable=False)
    __apellido= db.Column(db.String(100), nullable=False)
    __ID=db.Column(db.Integer, primary_key=True)

    #setters

    def set_nombre(self, nombre):
        self.__nombre=nombre

    def set_apellido(self, apellido):
        self.__apellido=apellido
    
    def set_usuario(self, usuario):
        #considerar control para que el usuario sea único
        self.__usuario=usuario

    def set_contraseña(self, contraseña):
        self.__contraseña=contraseña

    def set_email(self, email):
        #considerar control para que el mail sea único
        self.__email=email

#Galileo=Usuario()
#Galileo.contraseña=ksjdsk
#Galileo.set_contraseña(kajsks)

    #getters

    def get_nombre(self):
        return self.__nombre

    def get_apellido(self):
        return self.__apellido
    
    def get_usuario(self):
        return self.__usuario

    def get_contraseña(self):
        return self.__contraseña

    def get_email(self):
        return self.__email





###control de errores

from sqlalchemy.exc import IntegrityError

new_user = User(name='John Doe', email='johndoe@example.com')

try:
    session.add(new_user)
    session.commit()
    print("Objeto guardado en la base de datos:", new_user)
except IntegrityError:
    session.rollback()
    print("Error: El email ya está en uso.")
