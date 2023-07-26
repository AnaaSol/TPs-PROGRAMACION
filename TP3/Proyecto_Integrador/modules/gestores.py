import pickle as p
from modules.config import db
from modules.databases import Reclamo_db, Persona_db
from modules.reclamo import Reclamo
from modules.clasificador import Clasificador 
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import IntegrityError, InterfaceError
from modules.preprocesamiento import TextVectorizer

class Gestor_de_reclamos():

    def __init__(self, ruta):
        with open(ruta, 'rb') as archivo:
           self.__clasificador = p.load(archivo)

    def crear_reclamo(self, data): #data=[ID, description, fecha, user_id] + imagen 
        """Crea un reclamo con la información proporcionada por el usuario"""
        claim=Reclamo(data[0], data[1], data[2], data[3])
        try:
            claim.cargar_imagen(data[4])
        except:
            pass
        return claim #¿cómo se entera usuario?

    def clasificar_reclamo(self, claim):
        """Recibe el reclamo (objeto) y lo clasifica"""
        depto=self.__clasificador.clasificar([claim.get_descripcion])
        claim.set_depto(depto[0])

    def cargar_de_db(self, datos_reclamos): #datos_reclamos se obtiene de get_reclamos_by_filtro
        """Recibe los datos del o los reclamos y los crea, devolviendo una lista con los objetos"""
        reclamos=[]
        #datos_reclamos es una lista de datos donde datos=[ID_reclamo, description, timestap, ID_user, estado, depto, imagen, adherentes]
        try:
            for datos in datos_reclamos:
                claim=Reclamo(datos[0], datos[1], datos[2], datos[3])
                claim.cambiar_estado(datos[4])
                claim.set_depto(datos[5])
                claim.cargar_imagen(datos[6])
                if datos[7]!="": #evita un ValueError cuando int("")
                    for adh in datos[7].split(" "): 
                        claim.sumar_adherente(int(adh))
                reclamos.append(claim)
            return reclamos
        except IndexError:
            print("Recuerde utilizar el método get_reclamos_by_filtro() del Gestor de base de datos")

    def filtrar_por_depto(self, reclamos, filtro):
        """Recibe una lista con los reclamos a filtrar y un string como filtro y devuelve una lista con los objetos filtrados"""
        filtrados=[]
        for reclamo in reclamos:
            if reclamo.get_departamento==filtro:
                filtrados.append(reclamo)
        return filtrados

        
class Gestor_de_base_de_datos():
    """El gestor de base de datos consulta y modifica la información almacenada en la base de datos"""

    def __get_username_by_ID(self, id):
        try:
            user=db.session.query(Persona_db).filter_by(ID=id).one() #one() lanza error si encuentra más de uno o ninguno
            return user.username
        except NoResultFound:
            raise Exception("El usuario no existe")

    def __get_user_by_username(self, username):
        try:
            user=db.session.query(Persona_db).filter_by(username=username).one() #one() lanza error si encuentra más de uno o ninguno
            return user
        except NoResultFound:
            raise Exception("El usuario no existe")
        
    # def __get_reclamo_by_ID(self, ID):
    #     try:
    #         reclamo=db.session.query(Reclamo_db).filter_by(ID_reclamo=ID).one()
    #         return reclamo
    #     except NoResultFound:
    #         raise Exception("El reclamo no existe")
        
    def get_reclamos_by_filtro(self, type="all", filtro="ninguno"): 
        """Filtra los reclamos por departamento, estado o ID de usuario. Si no se especifica el tipo de filtro ni el
        valor del mismo, tomarán los valores default y se devolverán todos los reclamos en la base de datos"""
        type=type.lower()
        if type=="all" and filtro=="nada": #valores default
            reclamo=db.session.query(Reclamo_db).all()
        elif type=="usuario":
            reclamo=db.session.query(Reclamo_db).filter(Reclamo_db.ID_user==filtro).all() #filtro es el ID del usuario
            #si está vacía, either no existe un usuario con ese ID o no ha generado reclamos
            #(el primer caso se puede controlar con la obtención previa del ID)
        elif type=="estado":
            filtro=filtro.lower()
            if filtro in ["pendiente", "resuelto", "inválido", "en proceso"]:
                reclamo=db.session.query(Reclamo_db).filter(Reclamo_db.estado==filtro).all() 
            else:
                raise Exception("Filtro inválido")
        elif type=="departamento":
            filtro=filtro.lower()
            if filtro in ["soporte informático", "maestranza", "secretaría técnica"]:
                reclamo=db.session.query(Reclamo_db).filter(Reclamo_db.depto==filtro).all()
            else:
                raise Exception("Filtro inválido")
        elif type=="id":
            try: 
                reclamo=db.session.query(Reclamo_db).filter(Reclamo_db.ID_reclamo==filtro).one()
            except NoResultFound:
                raise Exception("El reclamo no existe")
        elif type=="id_usuario":
            try: 
                reclamo=db.session.query(Reclamo_db).filter(Reclamo_db.ID_user==filtro).all()
            except NoResultFound:
                raise Exception("El reclamo no existe")
        elif type=="adherente":
            reclamo=[]
            try:
                recl=db.session.query(Reclamo_db).all()
                for i in recl:
                    adherentes=i.adherentes
                    adherentes.split(" ")
                    if filtro in adherentes:
                        reclamo.append(i)
            except NoResultFound:
                raise Exception("No es un adherente") #no debería saltar esta excepción
        else:
            raise Exception("Sólo puede filtrar por usuario, departamento, estado o ID")
        
        #este bloque de código no se ejecuta si ocurre alguna excepción
        try:
            if len(reclamo)==0:
                return(reclamo) 
        except:
            if reclamo==None:
                return(reclamo)
        
        datos_reclamos=[]
        if type=="id":
            datos=[reclamo.ID_reclamo, reclamo.description, reclamo.timestap, reclamo.ID_user, reclamo.estado, reclamo.depto, reclamo.imagen, reclamo.adherentes]
            datos_reclamos.append(datos)
        else:
            for recl in reclamo: #TypeError: 'Reclamo_db' object is not iterable (one() devuelve el objeto, no dentro de una lista)
                datos=[recl.ID_reclamo, recl.description, recl.timestap, recl.ID_user, recl.estado, recl.depto, recl.imagen, recl.adherentes]
                datos_reclamos.append(datos)
        return datos_reclamos
    
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
            attribute=getattr(user, dato, "El atributo no existe") 
            #el valor default nunca debería devolverse por el control previo, pero lo dejo para prevenir un AttributeError
            return attribute
        else:
            raise Exception("El dato ingresado no corresponde a ningún atributo de user")
        
    # def get_dato_reclamo(self, ID_reclamo, dato): 
    #     if dato in ["ID_reclamo", "description", "estado", "depto", "timestap", "adherentes", "ID_user"]:
    #         reclamo=self.__get_reclamo_by_ID(ID_reclamo)
    #         attribute=getattr(reclamo, dato, None)
    #         return attribute
    #     else:
    #         raise Exception("Dato inválido")

    def contar_cantidad(self, depto):
        """Devuelve una lista con la cantidad de reclamos pendientes, inválidos, en proceso y resueltos del departamento solicitado"""
        reclamos_competentes=self.get_reclamos_by_filtro("departamento", depto)
        estado_reclamos_competentes=[reclamo[4] for reclamo in reclamos_competentes]
        pendiente=0
        invalido=0
        en_proceso=0
        resuelto=0
        for estado in estado_reclamos_competentes:
            estado=estado.lower()
            if estado=="pendiente":
                pendiente+=1
            elif estado=="inválido":
                invalido+=1
            elif estado=="resuelto":
                resuelto+=1
            elif estado=="en proceso":
                en_proceso+=1
        return [pendiente, invalido, en_proceso, resuelto]

#dato=[claim.get_ID(), claim.get_descripcion()...] ; claim=Reclamo()
    def guardar_nuevo_objeto(self, clase, dato): #dato debería ser una lista con el "formato" del objeto

        if clase in ["reclamo", "usuario", "jefe"]:

            try:

                if clase=="reclamo":
                    nuevo_reclamo=Reclamo_db(
                        description=dato[0], #str
                        estado=dato[1], #str
                        depto=dato[2], #str
                        timestap=dato[3], #str
                        ID_user=dato[4] #int
                        ) 

                    try: 
                        nuevo_reclamo.add_image(dato[5])
                    except IndexError: #no hay dato[5], es decir, imagen
                        pass

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

            except InterfaceError: #se intenta cargar un tipo de dato que no admite la columna
                print("Probablemente algún dato es de un tipo no compatible con su respectiva columna")
                #por alguna razón no salta error cuando se intenta guarda un entero en String(), creo que lo convierte

            except IntegrityError: #se intenta violar la restricción de unicidad
                print("Recuerde respetar la unicidad de email y nombre de usuario")

            except IndexError: #la lista no contiene todos los elementos requeridos
                print("Faltan datos")

            except Exception as e:
                print("Ha ocurrido una excepción:", e)

        else:
            print("No existe esa base de datos.")
    
    #hay que controlar externamente nuevo_valor o pueden pasar cosas malas
    def modificar_dato(self, dato, nuevo_valor, clase, ID):  #dato y clase son siempre strs, el ID es del objeto cuyo dato se quiere modificar
        """Modifica el dato del objeto provisto (ID y clase) si está permitido"""
        if clase.lower() in ["usuario", "reclamo"]:
            if clase=="reclamo":
                if dato in ["estado", "depto", "adherentes"]:
                    objeto=db.session.get(Reclamo_db, ID)
                else:
                    raise Exception("No puede modificar este atributo del reclamo")
            else:
                if dato in ["reclamos_adheridos", "reclamos_generados"]: #cambios de email, username y contraseña escapan de los requerimientos funcionales
                    objeto=db.session.get(Persona_db, ID)
                else:
                    raise Exception("No puede modificar este atributo del usuario")
            if objeto is not None:
                setattr(objeto, dato, nuevo_valor) #sólo funciona si el atributo es público
               #objeto.dato=nuevo_valor ; si dato no existe como atributo, lo crea y le asigna nuevo_valor
                db.session.commit()
                print("Cambio guardado")
        else:
            raise Exception("No existe una base de datos para esa clase o no se permite modificarla")
 
        def eliminar(self, ID, tipo):
            if tipo=="reclamo":
                reclamo = db.session.get(Reclamo_db, ID)
                if reclamo:
                    db.session.delete(reclamo)  
                    db.session.commit()
                    print("Se ha eliminado con éxito")
            elif tipo=="jefe" or tipo=="usuario":
                persona = db.session.get(Persona_db, ID)
                if persona:
                    db.session.delete(persona)
                    db.session.commit()
                    print("Se ha eliminado con éxito")

        

