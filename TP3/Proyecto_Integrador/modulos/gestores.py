import pickle
from modulos.config import db
from modulos.databases import Reclamo_db, Persona_db
from modulos.reclamo import Reclamo
#from modulos.ClasificadorSk.clasificadorsk.modules.clasificador import Clasificador 
from sqlalchemy.orm.exc import NoResultFound
#from modulos.ClasificadorSk.clasificadorsk.modules.preprocesamiento import TextVectorizer

class Gestor_de_reclamos():

    def __init__(self, ruta):
        with open(ruta, 'rb') as archivo:
           self.__clasificador = pickle.load(archivo)

    def crear_reclamo(self, data): # data=[title, descrip, fecha, id_user] 
        """Crea un reclamo con la información proporcionada por el usuario"""
        claim=Reclamo(data)
        return claim #¿cómo se entera usuario?

    def clasificar_reclamo(self, claim):
         depto=self.__clasificador.clasificar(claim.get_descripcion)
         claim.set_depto(depto)

    def filtrar_reclamos(self, filtro, valor_filtro, reclamos):
        """Filtra los reclamos que recibe según un estado o departamento específico"""
        if filtro in ["depto", "estado"]:
            #chequea que el filtro y su valor se correspondan:
            if filtro=="depto" and valor_filtro in ["maestranza", "soporte informático"] or filtro=="estado" and valor_filtro in ["pendiente", "resuelto", "inválido", "en proceso"]:
                reclamos_filtrados=[]
                for reclamo in reclamos:
                    if getattr(reclamo, filtro)==valor_filtro:
                        reclamos_filtrados.append(reclamo)
                return reclamos_filtrados
            else:
                raise Exception("El valor del filtro no es válido")
        else:
            raise Exception("Sólo se puede filtrar por departamento o estado")

    def asignar_a_depto(self, reclamo, depto):
            """Se obtiene el departamento correspondiente de la base de datos con depto y se le asigna el reclamo"""

    def cargar_de_db(self, datos_reclamos): #datos_reclamos se obtiene de 
        for reclamo in datos_reclamos:
            claim=Reclamo(reclamo[0], reclamo[1], reclamo[2])
            claim.set_depto(reclamo[3])


class Gestor_de_base_de_datos():
    """El gestor de base de datos consulta y modifica la información almacenada en la base de datos"""
    
    def __get_user_by_username(self, username):
        try:
            user=db.session.query(Persona_db).filter_by(username=username).one()
            return user
        except NoResultFound:
            raise Exception("El usuario no existe")
        
    def __get_reclamo_by_filtro(self, filtro): #filtra los reclamos por depto o estado
        filtro=filtro.lower()
        if filtro in ["pendiente", "resuelto", "en proceso", "inválido"]:
            reclamos=db.session.query(Reclamo_db).filter(estado=filtro).all()
            return reclamos
        elif filtro in ["soporte informático", "maestranza"]:
            reclamos=db.session.query(Reclamo_db).filter(depto=filtro).all()
            return reclamos
        else:
            raise Exception("Filtro inválido. Ingrese un departamento o estado.")
    
    def chequear_disponibilidad(self, respecto_de, valor):
        """Chequea la disponibilidad de un email o nombre de usuario"""
        respecto_de=respecto_de.lower()
        if respecto_de in ["email", "username"]:
            users=db.session.query(Persona_db).all()
            atributos=[]
            for user in users:
                atributos.append(getattr(user, respecto_de))
            if valor in atributos:
                return "Email/usuario ocupado"
            else:
                return "Email/usuario disponible"
        else:
            print("El dato no necesita ser único")
    
    def get_dato_user(self, username, dato):
        """Recibe el nombre de usuario y el dato a consultar y devuelve el valor del mismo, si el usuario existe y el dato es válido"""
        if dato in ["ID", "email", "username", "password", "name", "surname", "depto", "claustro", "reclamos_adheridos", "reclamos_generados"]:
            user=self.__get_user_by_username(username)
            attribute=getattr(user, dato, None)
            return attribute
        else:
            raise Exception("El dato ingresado no corresponde a ningún atributo de user")

    def reclamos_de_user(self, username):
        """Devuelve los reclamos generados por el usuario de interés"""
        ID_required_user=self.get_dato_user(username, "ID")
        reclamos=db.session.query(Reclamo_db).filter(Reclamo_db.ID_user==ID_required_user).all() #sólo se puede hacer si los atributos son públicos
        datos_reclamos=[]
        for reclamo in reclamos:
            datos=(reclamo.description, reclamo.timestap, reclamo.ID_user, reclamo.depto, reclamo.adherentes, reclamo.estado)
            datos_reclamos.append(datos)
        return datos_reclamos  

#dato=[claim.get_ID(), claim.get_descripcion()...] ; claim=Reclamo()
    def guardar_nuevo_objeto(self, clase, dato): #dato debería ser una lista con el "formato" del objeto
        if clase=="reclamo":
            nuevo_reclamo=Reclamo_db(
                description=dato[0], #str
                estado=dato[1], #str
                depto=dato[2], #str
                timestap=dato[3], #str
                adherentes=dato[4], #str
                id_user=dato[5] #int
                ) 
            db.session.add(nuevo_reclamo)
            db.session.commit()
            
        elif clase=="usuario":
            nuevo_usuario=Persona_db(
                name=dato[0],
                surname=dato[1],
                email=dato[2],
                username=dato[3], 
                password=dato[4],
                )
            nuevo_usuario.set_claustro(dato[5])
            nuevo_usuario.set_reclamos(dato[6], "generados")
            nuevo_usuario.set_reclamos(dato[7], "adheridos")
            db.session.add(nuevo_usuario)
            db.session.commit()

        elif clase=="jefe":
            nuevo_jefe=Persona_db( #se inicializa con elementos del __init__
                name=dato[0],
                surname=dato[1],
                username=dato[2],
                email=dato[3], 
                password=dato[4],
                )
            nuevo_jefe.set_depto(dato[5]) #se utilizan setters para atributos particulares
            db.session.add(nuevo_jefe)
            db.session.commit()

        else:
            print("No existe esa base de datos.")
    
    def modificar_dato(self, dato, nuevo_valor, clase, ID): 
        if clase in ["jefe", "usuario", "reclamo"]:
            if clase=="reclamo":
                objeto=db.session.get(Reclamo_db, ID)
            else:
                objeto=db.session.get(Persona_db, ID)

            if objeto is not None:
                setattr(objeto, dato, nuevo_valor)
                db.session.commit()
                print("Cambio guardado")
        else:
            raise Exception("No existe una base de datos para esa clase")


#consultar query en : 
# https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwjSpfHw3Oz_AhXmrJUCHZxeC18QFnoECA4QAQ&url=https%3A%2F%2Fdocs.sqlalchemy.org%2F14%2Form%2Fquery.html&usg=AOvVaw3Gtd4wgYBsOHKGfN3V9ZO2&opi=89978449