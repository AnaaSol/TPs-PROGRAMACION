class Persona:
    def __init__(self):
        self.DNI=""
        self.nombre=""
        self.apellido=""
        self.usuario=""
        self.contraseña=""
        self.mail=""
        self.claustro=""
    def cambiar_datos(self):
        pass
    def logging(self):
        pass

class Usuario(Persona):
    def __init__(self):
        self.ID=""
        self.reclamos_adheridos=[]
    def crear_usuraio(self):
        pass
    def generar_reclamo(self):
        pass
    def adherirse_a_reclamo(self):
        pass

class Jefes(Persona):
    def __init__(self):
        self.departamento=""    # ¿puede pertenecer a más de un departamento?
    def leer_reclamo(self):
        pass
    def manejar_reclamo(self):
        pass
    def derivar_reclamo(self):
        pass
    def generar_reporte(self):
        pass

class Gestor_de_Reclamos:
    def __init__(self):
        self.reclamo=""
    def clasificar(self):
        pass

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
        self.reclamos=[]
    def crear_depto(self):
        pass
    def cambiar_jefe(self):
        pass
