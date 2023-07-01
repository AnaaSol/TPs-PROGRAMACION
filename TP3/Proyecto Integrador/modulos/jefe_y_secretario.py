from persona import Persona

class Jefe(Persona):

    def __init__(self, ID, nombre, apellido, usuario, email, contraseña, depto):
        self._ID=ID #etiqueta única que se obtiene en databases con primary_key
        self._nombre=nombre
        self._apellido=apellido
        self._usuario=usuario
        self._contraseña=contraseña
        self._email=email
        self.__departamento=depto   
    
    def set_departamento(self, depto):
        self.__departamento=depto

    def get_departamento(self):
        return self.__departamento

    def manejar_reclamo(self, reclamo, estado):
        """Actualiza el estado del reclamo"""
        reclamo.cambiar_estado(estado)

    def generar_reporte(self):
        pass

class Secretario(Jefe):
    
    def derivar_reclamo(self):
        """Deriva el reclamo"""