#from modulos.config import db #no encuentra modulos
from config import db, app #como los archivos están dentro de la misma carpeta, no pongo el nombre de la misma ("modulos")
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
    #tuve problemas con los ARRAY y no pude descubrir por qué
    # reclamos_adheridos = db.Column(db.ARRAY(db.Integer())) #arreglo (lista) de enteros
    # reclamos_generados = db.Column(db.ARRAY(db.Integer()))
    #atributos de jefe
    depto = db.Column(db.String(100))
    #columna discriminante
    #type=db.Column(db.String(50)) #¿es necesaria? podríamos filtrar por depto ; if depto=None, persona es un usuario final

    def __init__(self, ID, email, username, password, name, surname):
        self.ID=ID
        self.email=email
        self.username=username
        self.password=password
        self.name=name
        self.surname=surname

    def get_password(self):
        return self.__password

class Reclamo_db(db.Model):

    __tablename__='reclamos'

    ID_reclamo = db.Column(db.Integer(), primary_key=True) #no los reconoce con doble guion bajo al principio
    description = db.Column(db.String(10000), nullable=False)
    estado = db.Column(db.String(10))
    depto = db.Column(db.String(25))
    timestap = db.Column(db.String(50), nullable=False)
    adherentes = db.Column(db.String())
    title = db.Column(db.String(100), nullable=False)
    ID_user = db.Column(db.Integer(), db.ForeignKey('personas.ID'))

from flask_login import login_user, login_required, current_user, logout_user
from flask import abort
from functools import wraps

admin_list=[1]

with app.app_context():
    db.drop_all()
    db.create_all()

    Paula=Persona_db(
    ID = 1,
    email = "paulabelendemartini2@gmail.com",
    username = "paudem",
    password = "tuqui",
    name = "Paula",
    surname= "Demartini"
    #usuario final sin reclamos adheridos ni generados
    )

    Ana=Persona_db(
    ID = 2,
    email = "anasolm26@gmail.com",
    username = "anasolm",
    password = "anosé",
    name = "Ana",
    surname= "Murzi"
    #usuario final sin reclamos adheridos ni generados
    )

    #print(Paula.ID) #salida: 1
    #print(Paula.__password) #error
    #print(Paula.get_password()) #salida: tuqui
    db.session.add(Paula)
    db.session.commit()
    db.session.add(Ana)
    db.session.commit()

    # print(db.session.query(Persona_db).all()) #no sé por qué los imprime con coma al final
    # print(db.session.query(Persona_db.email).all())
    # print(db.session.get(Persona_db, 1))
    user=db.session.get(Persona_db, 1)
    print(user.name) #primera vez que carga de base de datos
    print(user.surname)
    print(user.get_password())
    # print(user.claustro)
    # print("La contaseña original es:", user.password)
    # user.password="estamos en problemas" #rompí el encapsulamiento
    # print("Cambio de contraseña:", user.password)
    # user_again=db.session.get(Persona_db, 1) #segunda vez que carga de base de datos
    # print("Contraseña del usuario cargado de la base de datos de vuelta:", user_again.password)
    # print(db.session.query(Persona_db.username).filter(Persona_db.name=="Ana"))

    # from usuario import Usuario
    # Paulita=Usuario(user.ID, user.name, user.surname, user.username, user.email, user.password, user.claustro)
    # print(Paulita.get_email())

def admin_only(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if current_user.is_authenticated and current_user.id not in admin_list:
            return abort(403)
        return f(*args, **kwargs)
    return decorated_function

def is_admin():
    if current_user.is_authenticated and current_user.id in admin_list:
        return True
    else:
        return False


