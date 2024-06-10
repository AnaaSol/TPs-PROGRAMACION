from modules.persona import Persona
class Prueba:
    def __init__(self):
        self.__id = 1122

    def get_ID(self):
        return self.__id
    
class Jefe(Persona):

    def __init__(self, ID, nombre, apellido, usuario, email, contraseña, depto):
        super().__init__(ID, nombre, apellido, usuario, email, contraseña)
    
        # self._ID=ID #etiqueta única que se obtiene en databases con primary_key
        # self._nombre=nombre
        # self._apellido=apellido
        # self._usuario=usuario
        # self._contraseña=contraseña
        # self._email=email
        self.__departamento=depto   
        
    def set_departamento(self, depto):
        self.__departamento=depto

    def get_departamento(self):
        return self.__departamento

def obtener_ID(objeto_con_get_ID):
    return objeto_con_get_ID.get_ID()

if __name__=="__main__":
    Yo=Jefe(14, "Luana", "Cabrera", "lucab", "luanacab@gmail.com", "hola1234", "maestranza")

    prueba = Prueba()

    print(obtener_ID(Yo))
    print(obtener_ID(prueba))