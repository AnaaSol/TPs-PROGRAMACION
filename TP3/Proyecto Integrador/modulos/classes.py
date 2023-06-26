import datetime
from abc import ABC, abstractmethod
import pickle
from ClasificadorSk.clasificadorsk.modules.clasificador import Clasificador as ClasificadorIA
from ClasificadorSk.clasificadorsk.modules.preprocesamiento import TextVectorizer

class Persona(ABC):
    @abstractmethod #debería ser abstracto si no varía en las clases hijas?
    def __init__(self, ID):
        self.__id=ID #etiqueta única que se obtiene en databases con primary_key
        self.__nombre=""
        self.__apellido=""
        self.__usuario=""
        self.__contraseña=""
        self.__mail=""

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

    def set_mail(self, mail):
        #considerar control para que el mail sea único
        self.__mail=mail

#Galileo=Usuario()
#Galileo.set_contraseña(kajsks)
    
    #getters

    def get_nombre(self):
        return self.__nombre

    def get_apellido(self):
        return self.__apellido
    
    def get_usuario(self, usuario):
        return self.__usuario

    def get_contraseña(self, contraseña):
        return self.__contraseña

    def get_mail(self, mail):
        return self.__mail
    
    #¿no pueden cambairse los datos con los setters?
    def cambiar_datos(self, dato_a_cambiar, nuevo):
        #debería pedir la contraseña antes de permtiir hacer cambios
        if dato_a_cambiar == "mail":
            #debería chequear que el mail no esté ocupado
            self.__mail=nuevo
        elif dato_a_cambiar == "contraseña":
            self.__contraseña=nuevo
        

class Usuario(Persona):
    def __init__(self):
        self.__claustro=""
        self.__reclamos_adheridos=[] 
        self.__reclamos_generados=[] #quizás debería guardar el id de los reclamos una vez creados como objetos

    def set_claustro(self, claustro):
        self.__claustro=claustro

    def get_claustro(self):
        return self.__claustro

    def generar_reclamo(self, nombre_reclamo, descripcion):
        reclamo=[nombre_reclamo, descripcion, "(datetime.datetime.now())[:19]"]
        self.__reclamos_generados.append(reclamo)
        return reclamo.append(self.__id)
    
    def adherirse_a_reclamo(self, reclamo): #recibe el objeto 
        self.__reclamos_adheridos.append(reclamo.get_title)
        reclamo.sumar_adherente(self.__nombre)

class Jefe(Persona):
    def __init__(self):
        self.__departamento=""   
    
    def set_departamento(self, depto):
        self.__departamento=depto

    def get_departamento(self):
        return self.__departamento

    def manejar_reclamo(self, reclamo, estado):
        """Actualiza el estado del reclamo"""
        reclamo.cambiar_estado(estado)

    def derivar_reclamo(self): #sólo es función del secretario técnico
        pass

    def generar_reporte(self): 
        pass

class Reclamo(): 
    def __init__(self, title, description, fecha, user_id, ID): #todos estos datos se obtienen de Usuario.generar_reclamo()
        self.__title=title
        self.__ID=ID #etiqueta única generado en databases con primary_key
        self.__ID_usuario=user_id
        self.__descripcion=description
        self.__estado="Pendiente" #por default
        self.__departamento=""
        self.__date=fecha
        self.__adherentes=[]

    def set_depto(self, depto):
        self.__departamento=depto

    def cambiar_estado(self, estado):
        self.__estado=estado

    #getters

    def get_title(self):
        return self.__title

    def get_description(self):
        return self.__descripcion
    
    def get_ID(self):
        return self.__ID
    
    def get_estado(self):
        return self.__estado
    
    def get_ID(self):
        return self.__ID
    
    def get_ID_usuario(self):
        return self.__ID_usuario
    
    def get_departamento(self):
        return self.__departamento

    def sumar_adherente(self, adherente):
        self.__adherentes.append(adherente)

    def contar_adherentes(self):
        return len(self.__adherentes)

class Departamento():
    def __init__(self, nombre, jefe):
        self.__jefe=jefe
        self.__reclamos_correspondientes=[]
        self.__nombre=nombre

    def cambiar_jefe(self, jefe):
        self.__jefe=jefe

    def añadir_reclamo(self, reclamo):
        if isinstance(reclamo, Reclamo):
            self.__reclamos_correspondientes.append(reclamo)
            reclamo.set_depto(self.__nombre)

class Clasificador():
    def __init__(self):
        self.clasificador=ClasificadorIA()

    def Clasifica(self, reclamo):
        if isinstance(reclamo, Reclamo):
            texto=reclamo.get_description
            depto=self.clasificador.clasificar(texto)
            return depto

class Gestor_de_reclamos():

    def __init__(self):
        self.__reclamos=[]

    def crear_depto(self, data):
        """Crea un reclamo con la información proporcionada por el usuario"""

    def asignar_a_depto(self, reclamo):
        if isinstance(reclamo, Reclamo):
            texto=reclamo.get_description
            depto=self.__clasificador(texto)
            reclamo.set_depto=depto
            return depto
    

    def agregar_reclamo(self, reclamo):
        if isinstance(reclamo, Reclamo):
            self.__reclamos.append(reclamo)

    def asignar_a_depto(self):
        for claim in self.__reclamos

        

    