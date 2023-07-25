#from modulos.config import db #no encuentra modulos
from modules.config import db, app #como los archivos están dentro de la misma carpeta, no pongo el nombre de la misma ("modulos")
from flask_login import UserMixin


#los valores de los atributos para cada instancia se pueden inicializar gracias a un posible "__init__" dentro de db.Model;
#por lo que no pueden ser "privados" (este tipo de atributos se acceden sólo desde la clase), sino protegidos:
#esto considera la herencia y permite que los atributos sean accededidos por las clases hijas

class Persona_db(db.Model):
    
    __tablename__='personas'

    #atributos comunes
    ID=db.Column(db.Integer(), primary_key=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    surname= db.Column(db.String(100), nullable=False)
    #atributos de usuario
    claustro = db.Column(db.String(100))
    # reclamos_adheridos = db.Column(db.String()) #string de ID's separados por comas o espacios
    # reclamos_generados = db.Column(db.String())
    #atributos de jefe
    depto = db.Column(db.String(100))
    #columna discriminante
    #type=db.Column(db.String(50)) #¿es necesaria? podríamos filtrar por depto ; if depto=None, persona es un usuario final

#al init pasarle sólo atributos comunes
    def __init__(self, email, username, password, name, surname): #cuando instancio utilizo estos nombres (keyword argument)
        self.email=email
        self.username=username
        self.password=password
        self.name=name
        self.surname=surname
        #atributos característicos = None a menos que se cambien después
        self.depto=None
        self.claustro=None
        # self.reclamos_generados=None
        # self.reclamos_adheridos=None

    def set_depto(self, depto):
        self.depto=depto

    def set_claustro(self, claustro):
        self.claustro=claustro

    def set_reclamos(self, reclamos, relationship):
        if relationship=="adheridos":
            self.reclamos_adheridos=reclamos
        elif relationship=="generados":
            self.reclamos_generados=reclamos
        else:
            print("Sólo puede cargar los reclamos generados por el usuario o aquellos a los que adhirió")

class Reclamo_db(db.Model):

    __tablename__='reclamos'

    ID_reclamo = db.Column(db.Integer(), primary_key=True) 
    description = db.Column(db.String(10000), nullable=False)
    estado = db.Column(db.String(10))
    depto = db.Column(db.String(25))
    timestap = db.Column(db.String(50), nullable=False)
    adherentes = db.Column(db.String()) #string de ID's separados por espacios
    ID_user = db.Column(db.Integer(), db.ForeignKey('personas.ID'))
    imagen = db.Column(db.LargeBinary)

    def __init__(self, description, depto, timestap, estado, ID_user): #cuando instancio utilizo estos nombres
        self.depto=depto
        self.description=description
        self.timestap=timestap
        self.adherentes=""
        self.estado=estado
        self.ID_user=ID_user
        self.image=None

    def add_image(self, image):
        self.image=image

    #print(user_by_email.get_password())
    #print(user_by_email.ID)
    #user_1_password=db.session.query(Persona_db.get_password()).filter(Persona_db.ID==1) #get_password() requiere la instancia (self)
    #user=db.session.get(Persona_db, 1) #sólo acepta como identificador la clave primaria
    #print(user.name) #primera vez que carga de base de datos
    #print(user.surname)
    #print(user.get_password())

    # from usuario import Usuario
    # Paulita=Usuario(user.ID, user.name, user.surname, user.username, user.email, user.password, user.claustro)
    # print(Paulita.get_email())

#para obtener los reclamos creados por un usuario específico
#ID_required_user="ID del usuario solicitado"
#reclamos=db.session.query(Reclamo_db).filter(Reclamo_db.ID_user==ID_required_user) #sólo se puede hacer si los atributos son públicos
