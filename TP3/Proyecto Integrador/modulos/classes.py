import random
import datetime
from abc import ABC, abstractmethod

class Persona(ABC):
    @abstractmethod
    def __init__(self):
        self.nombre=""
        self.apellido=""
        self.usuario=""
        self.contraseña=""
        self.mail=""
        self.claustro=""

    def set_nombre(self, nombre):
        self.nombre=nombre
        return nombre

    def set_apellido(self, apellido):
        self.apellido=apellido
        return apellido
    
    def set_usuario(self, usuario):
        if isinstance (usuario, Persona):
            return "No es posible"
            #raise Exception ("Ya existe un usario con este nombre, por favor, ingresar otro")
        else:
            self.usuario=usuario
            return usuario

    def set_contraseña(self, contraseña):
        self.contraseña=contraseña
        return contraseña

    def set_mail(self, mail):
        if isinstance (mail, Persona):
            return "No es posible"
            #raise Exception ("Ya existe una cuenta con este mail, iniciar sección o ingresar uno distinto")
        else:
            self.mail=mail
            return mail
    
    def set_claustro(self, claustro):
        self.usuario=claustro
        return claustro
    
    def cambiar_datos(self, dato_a_cambiar, nuevo):
        if dato_a_cambiar == "mail":
            if isinstance (nuevo, Persona):
                raise Exception ("Ya existe una cuenta con este mail, iniciar sección o ingresar uno distinto")
            else:
                self.mail=nuevo
        elif dato_a_cambiar == "contraseña":
            self.contraseña=nuevo
        else:
            raise Exception ("No es posible modificar el tipo de dato ingresado")


class Usuario(Persona):
    def __init__(self):
        self.ID=random.randint(100000000, 999999999)
        self.reclamos_adheridos=[]
        self.reclamos_generados=[]


    def generar_reclamo(self, nombre_reclamo, descripcion):
        self.reclamos_generados.append([nombre_reclamo, descripcion, (datetime.datetime.now())[:19]])
        reclamo=[nombre_reclamo, descripcion, (datetime.datetime.now())[:19]]
        return reclamo
    
    def adherirse_a_reclamo(self, nombre_reclamo):
        self.reclamos_adheridos.append(nombre_reclamo)

class Jefes(Persona):
    def __init__(self):
        self.departamento=""    # ¿puede pertenecer a más de un departamento?
    
    def set_departamento(self, depto):
        self.departamento=depto

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
        self.ID=""
        self.ID_usuario=""
        self.descripcion=""
        self.estado=""
        self.departamento=""
        self.fecha_hora=""
        self.nro_adherentes=""
    def contar_adherentes(self):
        pass

class Departamento:
    def __init__(self):
        self.jefe=""
        self.reclamos_depto=[]
        self.nombre=""

    def crear_depto(self, nombre_departamento):
        self.nombre=""

    def asignar_jefe(self, jefe):
        if self.jefe=="":
            self.jefe=jefe
        else:
            raise Exception (self.jefe, "es el jefe de este departamento, si desea cambiarlo, utilizar cambiar_jefe()")

    def cambiar_jefe(self, jefe):
        if self.jefe=="":
            raise Exception ("Este departamento no tiene jefe, asignarlo con asignar_jefe")
        else:
            self.jefe=jefe

    def reclamos(self, reclamo):
        self.reclamos_depto.append(reclamo)
