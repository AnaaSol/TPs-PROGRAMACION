class Reclamo(): 
    def __init__(self, ID, description, fecha, user_id): #despues agregar imagen
        self.__ID=ID #etiqueta única generado en databases con primary_key; debería pasarse como atributo para crearlo, no arranca vacío
        self.__ID_usuario=user_id
        self.__descripcion=description
        self.__imagen=None
        self.__estado="pendiente" #por default
        self.__departamento=""
        self.__date=fecha
        self.__adherentes=[] #lista con los ID de los usuarios adheridos

    def cargar_imagen(self, data_image):
        self.__imagen=data_image

    def set_depto(self, depto):
        self.__departamento=depto

    def cambiar_estado(self, estado):
        self.__estado=estado

    #getters

    @property #para poder acceder a los atributos en HTML
    def get_descripcion(self):
        return self.__descripcion
    
    @property
    def get_ID(self):
        return self.__ID
    
    @property
    def get_estado(self):
        return self.__estado
    
    @property
    def get_ID_usuario(self):
        return self.__ID_usuario
    
    @property
    def get_departamento(self):
        return self.__departamento
    
    @property
    def get_fecha(self):
        return self.__date
    
    @property
    def get_imagen(self):
        return self.__imagen

    @property
    def get_adherentes(self):
        return self.__adherentes

    def sumar_adherente(self, adherente):
        self.__adherentes.append(adherente)

    @property 
    def contar_adherentes(self):
        return len(self.__adherentes)
    
# reclamo=Reclamo(1, "Me gusta la torta frita", "2023-07-19 15:31:19", 2)
# print(reclamo.get_adherentes)
# print(reclamo.contar_adherentes)
# reclamo.sumar_adherente(2)
# print(reclamo.get_adherentes)
# print(reclamo.contar_adherentes)
# reclamo.sumar_adherente(3)
# reclamo.sumar_adherente(4)
# print(reclamo.get_adherentes)
# print(reclamo.contar_adherentes)


type=None

if not type:
    print("Type es igual a None")
    print(type)
else:
    print("Type tiene un valor distinto de None")