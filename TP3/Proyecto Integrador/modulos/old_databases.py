#from modulos.config import db #no encuentra modulos
from config import db #como los archivos están dentro de la misma carpeta, no pongo el nombre de la misma ("modulos")
from flask_login import UserMixin

#los valores de los atributos para cada instancia se pueden inicializar gracias a un posible "__init__" dentro de db.Model;
#por lo que no pueden ser "privados" (este tipo de atributos se acceden sólo desde la clase), sino protegidos:
#esto considera la herencia y permite que los atributos sean accededidos por las clases hijas

class Persona_db(db.Model):
    
    __tablename__='personas'

    ID=db.Column(db.Integer(), primary_key=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    surname= db.Column(db.String(100), nullable=False)
    type=db.Column(db.String(50))

    __mapper_args__ = {
        "polymorphic_identity": "persona", #¿tiene sentido si la clase original (no la modelo) es abstracta?
#Este argumento especifica la identidad polimórfica del modelo base: 
#cuando se almacenan o recuperan objetos de la tabla, se consideran como objetos del tipo "persona"
        "polymorphic_on": type,
#Este argumento especifica la columna "type" que se utilizará para determinar el tipo de objeto en la jerarquía de 
#herencia. Cuando se almacena un objeto Persona en la base de datos, se guardará un valor correspondiente al tipo del 
#objeto en la columna "type" (usuario o jefe). 
# Luego, al recuperar objetos de la base de datos, SQLAlchemy utilizará este valor para determinar qué subclase 
# específica de Persona debe instanciar.
    }

class Usuario_db(Persona_db, UserMixin):

    __tablename__ = 'users'

    ID_usuario = db.Column(db.Integer(), db.ForeignKey('personas.ID'), primary_key=True)
    claustro = db.Column(db.String(100), nullable=False)
    reclamos_adheridos = db.Column(db.ARRAY(db.Integer)) #arreglo (lista) de enteros
    reclamos_generados = db.Column(db.ARRAY(db.Integer))

    __mapper_args__ = {
        "polymorphic_identity": "usuario",
    }

class Jefe_db(Persona_db, UserMixin):

    __tablename__ = 'jefes'

    ID_jefe=db.Column(db.Integer(), db.ForeignKey('personas.ID'), primary_key=True)
    depto = db.Column(db.String(100))

    __mapper_args__ = {
        "polymorphic_identity": "jefe",
    }

Javier=Jefe_db(
     ID_jefe=1,
     depto="Informática"
 )
print(Javier)

class Reclamo_db(db.Model):

    __tablename__='reclamos'

    ID_reclamo = db.Column(db.Integer(), primary_key=True) #no los reconoce con doble guion bajo al principio
    description = db.Column(db.String(10000), nullable=False)
    estado = db.Column(db.String(10))
    depto = db.Column(db.String(25))
    timestap = db.Column(db.String(50))
    adherentes = db.Column(db.String())
    title = db.Column(db.String(100), nullable=False)
    ID_user = db.Column(db.Integer(), db.ForeignKey('users.id'))
