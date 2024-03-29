from modules.persona import Persona
import datetime

class Usuario(Persona):

    def __init__(self, ID, nombre, apellido, usuario, email, contraseña, claustro):
        self._ID=ID #etiqueta única que se obtiene en databases con primary_key
        self._nombre=nombre
        self._apellido=apellido
        self._usuario=usuario
        self._contraseña=contraseña
        self._email=email
        self.__claustro=claustro
        self.__reclamos_adheridos=[] #lista con el ID de los reclamos adheridos
        self.__reclamos_generados=[] #lista con el ID de los reclamos generados

    def set_claustro(self, claustro):
        self.__claustro=claustro

    def get_claustro(self):
        return self.__claustro
    
    def get_reclamos_generados(self):
        return self.__reclamos_generados
    
    def get_reclamos_adheridos(self):
        return self.__reclamos_adheridos
    
    def guardar_reclamo_creado(self, ID):
        self.__reclamos_generados.append(ID)

    def generar_datos_reclamo(self, descripcion):
        reclamo=[descripcion, str(datetime.datetime.now())[:19], self._ID]
        return reclamo
    
    def adherirse_a_reclamo(self, reclamo_ID): 
        if reclamo_ID in self.__reclamos_adheridos:
            raise Exception("Usted ya está adherido a este reclamo")
        else: 
            self.__reclamos_adheridos.append(reclamo_ID)

#print(datetime.datetime.now()) #formato: year-month-day h:min:s.ms 
#print(str(datetime.datetime.now())[:19]) #pasamos el formato a str y hacemos un slice para sacar los milisegundos