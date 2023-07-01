class Departamento():
    def __init__(self, nombre, jefe):
        self.__jefe=jefe
        self.__reclamos_correspondientes=[]
        self.__nombre=nombre

    def cambiar_jefe(self, jefe):
        self.__jefe=jefe

    def añadir_reclamo(self, reclamo_ID):
        self.__reclamos_correspondientes.append(reclamo_ID)