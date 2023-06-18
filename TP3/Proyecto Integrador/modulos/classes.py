import random
import datetime
from abc import ABC, abstractmethod

class Persona(ABC):
    @abstractmethod
    def __init__(self):
        self.__nombre=""
        self.__apellido=""
        self.__usuario=""
        self.__contraseña=""
        self.__mail=""
        self.__claustro=""

    def set_nombre(self, nombre):
        self.__nombre=nombre
        return nombre

    def set_apellido(self, apellido):
        self.__apellido=apellido
        return apellido
    
    def set_usuario(self, usuario):
        if isinstance (usuario, Persona):
            raise Exception ("Ya existe un usario con este nombre, por favor, ingresar otro")
        else:
            self.__usuario=usuario
            return usuario

    def set_contraseña(self, contraseña):
        self.__contraseña=contraseña
        return contraseña

    def set_mail(self, mail):
        if isinstance (mail, Persona):
            raise Exception ("Ya existe una cuenta con este mail, iniciar sección o ingresar uno distinto")
        else:
            self.__mail=mail
            return mail
    
    def set_claustro(self, claustro):
        self.__claustro=claustro
        return claustro
    
    def cambiar_datos(self, dato_a_cambiar, nuevo):
        if dato_a_cambiar == "mail":
            if isinstance (nuevo, Persona):
                raise Exception ("Ya existe una cuenta con este mail, iniciar sección o ingresar uno distinto")
            else:
                self.__mail=nuevo
        elif dato_a_cambiar == "contraseña":
            self.__contraseña=nuevo
        else:
            raise Exception ("No es posible modificar el tipo de dato ingresado")


class Usuario(Persona):
    def __init__(self):
        self.__ID=random.randint(100000000, 999999999)
        while isinstance (self.__ID, Usuario):
            self.__ID=random.randint(100000000, 999999999)
        self.__reclamos_adheridos=[]
        self.__reclamos_generados=[]


    def generar_reclamo(self, nombre_reclamo, descripcion):
        self.__reclamos_generados.append([nombre_reclamo, descripcion, (datetime.datetime.now())[:19]])
        reclamo=[nombre_reclamo, descripcion, (datetime.datetime.now())[:19]]
        return reclamo
    
    def adherirse_a_reclamo(self, nombre_reclamo):
        self.__reclamos_adheridos.append(nombre_reclamo)

class Jefes(Persona):
    def __init__(self):
        self.__departamento=""    # ¿puede pertenecer a más de un departamento?
    
    def set_departamento(self, depto):
        self.__departamento=depto

    def leer_reclamo(self):
        pass
    def manejar_reclamo(self):
        pass
    def derivar_reclamo(self):
        pass
    def generar_reporte(self):
        pass

class Gestor_de_Reclamos:
    def clasificar(self, nombre_reclamo, descripcion):
        if "palabra clave" in nombre_reclamo:
            depto=""
        #...... repetir con varias palabras claves y hacer lo mismo con la descripcion
        return depto    

class Reclamo:
    def __init__(self):
        self.__ID=""
        self.__ID_usuario=""
        self.__descripcion=""
        self.__estado=""
        self.__departamento=""
        self.__fecha_hora=""
        self.__nro_adherentes=""
    def contar_adherentes(self):
        pass

class Departamento:
    def __init__(self):
        self.__jefe=""
        self.__reclamos_depto=[]
        self.__nombre=""

    def crear_depto(self, nombre_departamento):
        self.nombre=""

    def asignar_jefe(self, jefe):
        if self.__jefe=="":
            self.__jefe=jefe
        else:
            raise Exception (self.__jefe, "es el jefe de este departamento, si desea cambiarlo, utilizar cambiar_jefe()")

    def cambiar_jefe(self, jefe):
        if self.__jefe=="":
            raise Exception ("Este departamento no tiene jefe, asignarlo con asignar_jefe")
        else:
            self.__jefe=jefe

    def reclamos(self, reclamo):
        self.__reclamos_depto.append(reclamo)
