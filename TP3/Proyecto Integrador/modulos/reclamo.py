class Reclamo(): 
    def __init__(self, ID, description, fecha, user_id): #todos estos datos se obtienen de Usuario.generar_reclamo()
        self.__ID=ID #etiqueta única generado en databases con primary_key; debería pasarse como atributo para crearlo, no arranca vacío
        self.__ID_usuario=user_id
        self.__descripcion=description
        self.__estado="pendiente" #por default
        self.__departamento=""
        self.__date=fecha
        self.__adherentes=[] #lista con los ID de los usuarios adheridos

    def set_depto(self, depto):
        self.__departamento=depto

    def cambiar_estado(self, estado):
        self.__estado=estado

    #getters

    def get_descricion(self):
        return self.__descripcion
    
    def get_ID(self):
        return self.__ID
    
    def get_estado(self):
        return self.__estado
    
    def get_ID_usuario(self):
        return self.__ID_usuario
    
    def get_departamento(self):
        return self.__departamento
    
    def get_fecha(self):
        return self.__date

    def sumar_adherente(self, adherente):
        self.__adherentes.append(adherente)

    def contar_adherentes(self):
        return len(self.__adherentes)

type=None

if not type:
    print("Type es igual a None")
    print(type)
else:
    print("Type tiene un valor distinto de None")