#import pickle
from config import db
from databases import Reclamo_db, Persona_db
from reclamo import Reclamo
from ClasificadorSk.clasificadorsk.modules.clasificador import Clasificador as ClasificadorIA
#from ClasificadorSk.clasificadorsk.modules.preprocesamiento import TextVectorizer

class Gestor_de_reclamos():

    def __init__(self):
        self.__clasificador=ClasificadorIA()

    def crear_reclamo(self, data): # data=[title, descrip, fecha, id_user] 
        """Crea un reclamo con la información proporcionada por el usuario"""
        claim=Reclamo(data)
        return claim #¿cómo se entera usuario?

    def clasificar_reclamo(self, claim):
        depto=self.__clasificador.clasificar(claim.get_descripcion)
        claim.set_depto(depto)

    def asignar_a_depto(self, reclamo, depto):
            """Se obtiene el departamento correspondiente de la base de datos con depto y se le asigna el reclamo"""


class Gestor_de_base_de_datos():
    """El gestor de base de datos consultaría y modificaría la información almacenada en la base de datos en función de los requerimientos de demás clases"""
    
    def consultar_bd(self, atributo, clase):
        """Retorna el valor del atributo consultado"""
        value=db.session.query(clase.atributo).all()
        return value
    
    def cambiar_valor_atributo(self, nuevo_valor):
        pass

#dato=[claim.get_ID(), claim.get_descripcion()...] ; claim=Reclamo()
    def guardar_nuevo_objeto(self, clase, dato): #dato debería ser una lista con el "formato" del objeto
        if clase=="reclamo":
            nuevo_reclamo=Reclamo_db(
                ID_reclamo=dato[0], #int
                description=dato[1], #str
                estado=dato[2], #str
                depto=dato[3], #str
                timestap=dato[4], #str
                adherentes=dato[5], #str
                title=dato[6], #str
                id_user=dato[7] #int
                ) 
            db.session.add(nuevo_reclamo)
            db.session.commit()
            
        elif clase=="usuario":
            nuevo_usuario=Persona_db(
                ID=dato[0], 
                name=dato[1],
                surname=dato[2],
                username=dato[3],
                email=dato[4], 
                password=dato[5],
                claustro=dato[6],
                reclamos_adheridos=dato[7],
                reclamos_generados=dato[8]
                )
            db.session.add(nuevo_usuario)
            db.session.commit()

        elif clase=="jefes":
            nuevo_jefe=Persona_db(
                ID=dato[0], 
                name=dato[1],
                surname=dato[2],
                username=dato[3],
                email=dato[4], 
                password=dato[5],
                depto=dato[6],
                )
            db.session.add(nuevo_jefe)
            db.session.commit()

        else:
            print("No existe esa base de datos.")
    
    def modificar_dato(self, dato, clase): #por ejemplo, un usuario cambia la contraseña
        pass

#consultar query en : 
# https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwjSpfHw3Oz_AhXmrJUCHZxeC18QFnoECA4QAQ&url=https%3A%2F%2Fdocs.sqlalchemy.org%2F14%2Form%2Fquery.html&usg=AOvVaw3Gtd4wgYBsOHKGfN3V9ZO2&opi=89978449