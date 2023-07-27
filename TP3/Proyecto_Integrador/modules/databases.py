from modules.config import db, app 

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
    reclamos_adheridos = db.Column(db.String()) #string de ID's separados espacios
    reclamos_generados = db.Column(db.String())
    #atributos de jefe
    depto = db.Column(db.String(100))
    #actualizaciones
    actualizacion = db.Column(db.String())
    #columna discriminante: descartada
    
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
        self.reclamos_generados=None
        self.reclamos_adheridos=None
        #actualizaciones
        self.actualizacion="ninguna"

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
    actualizacion = db.Column(db.String())

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

#sólo se puede hacer consultas si los atributos son públicos
